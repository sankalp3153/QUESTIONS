

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0

        while i < len(words):
            # Determine how many words fit in the current line
            line_len = len(words[i])
            j = i + 1

            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])  # 1 for space
                j += 1

            line_words = words[i:j]
            num_of_words = j - i
            total_chars = sum(len(word) for word in line_words)

            # Calculate number of spaces to fill
            spaces_needed = maxWidth - total_chars

            if j == len(words) or num_of_words == 1:
                # Last line or only one word -> left-justified
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))  # pad remaining spaces
            else:
                spaces_between_words = spaces_needed // (num_of_words - 1)
                extra_spaces = spaces_needed % (num_of_words - 1)

                line = ''
                for k in range(num_of_words - 1):
                    line += line_words[k]
                    line += ' ' * (spaces_between_words + (1 if k < extra_spaces else 0))
                line += line_words[-1]  # last word, no space after

            res.append(line)
            i = j

        return res
