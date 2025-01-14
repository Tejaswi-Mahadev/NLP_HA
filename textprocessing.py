import re
from datetime import datetime

class TextAnalyzer:
    def __init__(self):
        # Regular expressions for articles
        self.article_patterns = {
            'a': r'\ba\b(?![-.]\b)',
            'an': r'\ban\b',
            'the': r'\bthe\b'
        }
        
        # Month names and their variations
        self.months = {
            'january': 1, 'jan': 1,
            'february': 2, 'feb': 2,
            'march': 3, 'mar': 3,
            'april': 4, 'apr': 4,
            'may': 5,
            'june': 6, 'jun': 6,
            'july': 7, 'jul': 7,
            'august': 8, 'aug': 8,
            'september': 9, 'sep': 9, 'sept': 9,
            'october': 10, 'oct': 10,
            'november': 11, 'nov': 11,
            'december': 12, 'dec': 12
        }
        
        # Compile date patterns
        self.date_patterns = [
            r'\b\d{1,2}[-/.]\d{1,2}[-/.]\d{2}(?:\d{2})?\b',
            r'\b\d{1,2}(?:st|nd|rd|th)?\s+(?:of\s+)?(?:' + 
            '|'.join(self.months.keys()) + 
            r')\s+\d{2}(?:\d{2})?\b',
            r'\b(?:' + '|'.join(self.months.keys()) + 
            r')\s+\d{1,2}(?:st|nd|rd|th)?,?\s+\d{2}(?:\d{2})?\b'
        ]
        
        self.compiled_date_patterns = [re.compile(pattern, re.IGNORECASE) 
                                     for pattern in self.date_patterns]

    def count_articles(self, text):
        """Count occurrences of articles in text."""
        results = {}
        for article, pattern in self.article_patterns.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            results[article] = len(matches)
        return results

    def count_dates(self, text):
        """Count valid dates in text."""
        dates = set()
        for pattern in self.compiled_date_patterns:
            matches = pattern.finditer(text)
            for match in matches:
                date_str = match.group()
                # Only add if it looks like a valid date
                if self._validate_date(date_str):
                    dates.add(date_str)
        return len(dates)

    def _validate_date(self, date_str):
        """Validate if the string represents a valid date."""
        # Convert month names to numbers
        date_lower = date_str.lower()
        for month_name, month_num in self.months.items():
            if month_name in date_lower:
                return True  # If we find a valid month name, consider it a valid date
        
        # Check numeric dates
        try:
            # Extract numbers from the string
            numbers = [int(n) for n in re.findall(r'\d+', date_str)]
            if len(numbers) == 3:  # Must have day, month, year
                year = max(numbers)  # Assume largest number is year
                numbers.remove(year)
                month = min(numbers)  # Assume smaller of remaining numbers is month
                numbers.remove(month)
                day = numbers[0]  # Last number is day
                
                # Basic validation
                if 1 <= month <= 12 and 1 <= day <= 31:
                    if year < 100:  # Two-digit year
                        year += 1900 if year >= 50 else 2000
                    return 1800 <= year <= 2100  # Reasonable year range
            return False
        except:
            return False

def main():
    try:
        # Read number of test cases
        T = int(input().strip())
        analyzer = TextAnalyzer()
        
        # Process each test case
        for _ in range(T):
            # Read text fragment
            text = input().strip()
            
            # Try to read blank line, but don't fail if it's not there
            try:
                input()
            except EOFError:
                pass  # Ignore EOF on blank line
            
            # Analyze text
            article_counts = analyzer.count_articles(text)
            date_count = analyzer.count_dates(text)
            
            # Print results for this test case
            print(article_counts['a'])
            print(article_counts['an'])
            print(article_counts['the'])
            print(date_count)
            
    except EOFError:
        pass  # Handle EOF gracefully

if __name__ == "__main__":
    main()
