import language_tool_python
import sys
import io
import jieba
import jieba.analyse
from transformers import pipeline
from summarizer import Summarizer

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def generate_summary(text, language_code):
    if language_code == 'zh-TW':
        try:
            # 使用 jieba 抓取關鍵字
            top_keywords = jieba.analyse.extract_tags(text, topK=3)
            
            # 分割文本成句子
            sentences = text.split('。')
            sentences = [s.strip() for s in sentences if s.strip()]

            # 選取包含關鍵字的句子
            summary_sentences = []
            for keyword in top_keywords:
                for sentence in sentences:
                    if keyword in sentence and sentence not in summary_sentences:
                        summary_sentences.append(sentence)
                        break

            # 組合摘要句子
            summary = '。'.join(summary_sentences) + '。'
            return summary
        except Exception as e:
            print(f"處理過程中出現錯誤: {e}")
            return "摘要生成失敗。"
    else:
        try:
            # 初始化 summarizer 和 LanguageTool
            summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            tool = language_tool_python.LanguageTool('en-US')

            # 使用 LanguageTool 修飾文本
            matches = tool.check(text)
            corrected_text = language_tool_python.utils.correct(text, matches)

            # 生成摘要
            summary = summarizer(corrected_text, max_length=100, min_length=30, do_sample=False)
            if not summary:
                print("無法生成有效的摘要。")
                return "摘要生成失敗。"
            return summary[0]['summary_text']
        
        except Exception as e:
            print(f"摘要生成過程中出現錯誤: {e}")
            return ""

if __name__ == "__main__":
    import sys
    input_text = sys.argv[1] if len(sys.argv) > 1 else "請提供一些文本。"
    language_code = sys.argv[2] if len(sys.argv) > 2 else "en-US"
    print(generate_summary(input_text, language_code))