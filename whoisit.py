import re
from collections import defaultdict

class AnaphoraResolver:
    def __init__(self):
        self.pronouns = {
            'masculine': {'he', 'him', 'his'},
            'feminine': {'she', 'her', 'hers'},
            'neuter': {'it', 'its'},
            'plural': {'they', 'them', 'their', 'theirs'}
        }
        
        self.subject_indicators = {
            'was', 'is', 'were', 'are', 'had', 'has', 'went', 'jumped',
            'looked', 'found', 'came', 'tried', 'opened', 'walked', 'said',
            'met', 'built', 'answered', 'huffed', 'puffed', 'knocked'
        }
        self.character_roles = {
            'protagonist': {'first', 'second', 'third', 'little', 'young'},
            'antagonist': {'wolf', 'hunter', 'witch'},
            'helper': {'man', 'fairy', 'dwarf'}
        }

    def _find_story_introduction(self, text):
        """Identify main characters from story introduction."""
        intro_match = re.search(r'once upon a time.*?[.!?]', text.lower())
        if intro_match:
            intro = intro_match.group(0)
            return intro
        return ""

    def _get_pronoun_windows(self, text, pronoun_pos, window_size=200):
        """Get text windows before and after pronoun for context."""
        start = max(0, pronoun_pos - window_size)
        end = min(len(text), pronoun_pos + window_size)
        return text[start:pronoun_pos], text[pronoun_pos:end]

    def _score_candidate(self, entity, pronoun, entity_pos, pronoun_pos, text):
        """Score a candidate antecedent based on multiple factors."""
        score = 0
        
        distance = pronoun_pos - entity_pos
        score -= distance * 0.1
        intro = self._find_story_introduction(text)
        if entity.lower() in intro.lower():
            score += 500
        before_text = text[max(0, entity_pos-50):entity_pos]
        after_text = text[entity_pos:min(len(text), entity_pos+50)]
        
        if any(indicator in after_text.split() for indicator in self.subject_indicators):
            score += 300
        entity_lower = entity.lower()
        for role_type, role_words in self.character_roles.items():
            if any(word in entity_lower for word in role_words):
                score += 200
        mentions = len(re.findall(r'\b' + re.escape(entity) + r'\b', text))
        score += mentions * 50
        
        return score

    def resolve_anaphora(self, text, entities):
        """Resolve pronouns to their antecedents."""
        pronouns = []
        resolved = []
        
      
        for match in re.finditer(r'\*\*(.*?)\*\*', text):
            pronouns.append((match.group(1), match.start()))
        
  
        current_context = {
            'last_subject': None,
            'last_mentioned': None
        }
        
      
        for pronoun, pos in pronouns:
            best_score = float('-inf')
            best_entity = None
            
          
            before_window, after_window = self._get_pronoun_windows(text, pos)
            
            
            for entity in entities:
               
                entity_matches = list(re.finditer(r'\b' + re.escape(entity) + r'\b', text[:pos]))
                if entity_matches:
                    entity_pos = entity_matches[-1].start()
                    score = self._score_candidate(entity, pronoun, entity_pos, pos, text)
                    
                    if score > best_score:
                        best_score = score
                        best_entity = entity
            
           
            if best_entity:
                current_context['last_mentioned'] = best_entity
                if any(indicator in after_window.split() for indicator in self.subject_indicators):
                    current_context['last_subject'] = best_entity
            
            resolved.append(best_entity if best_entity else "UNKNOWN")
        
        return resolved

def process_input():
    """Process input according to the specified format."""
    N = int(input())
    text = ""
    for _ in range(N):
        line = input().strip()
        text += line + " "
    entities = input().strip().split(";")
    return text, entities

def main():
    text, entities = process_input()
    resolver = AnaphoraResolver()
    results = resolver.resolve_anaphora(text, entities)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
