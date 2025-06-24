def wc(text):
   
    words = text.split()
    word_count = len(words)

    char_count = len(text)
    whitespace_count = sum(1 for c in text if c.isspace())

    return (word_count, char_count, whitespace_count)

sample = "Hello, world!\n이것은 테스트 문장입니다."
result = wc(sample)
print(result)  
