from logomachy.logomachy_text_stats.readability.base_readability import BaseReadability, ReadingLevel


class DaleChallReadabilityFormula(BaseReadability):
    """
    Provides a numeric gauge of the comprehension difficulty that readers come upon when reading a text.
    It uses a list of 3000 words that groups of fourth-grade American students could reliably understand,
    considering any word not on that list to be difficult.

    Score           Notes
    4.9 or lower    easily understood by an average 4th-grade student or lower
    5.0–5.9         easily understood by an average 5th or 6th-grade student
    6.0–6.9         easily understood by an average 7th or 8th-grade student
    7.0–7.9         easily understood by an average 9th or 10th-grade student
    8.0–8.9         easily understood by an average 11th or 12th-grade student
    9.0–9.9         easily understood by an average 13th to 15th-grade (college) student

    Description from https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula

    0.1579 x ((difficult words / total words) x 100) + 0.0496 x (total words / total sentences)
    """

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel.unknown
        text_info = self._text_analyser.get_text_info(text)
        words = text_info.word_count
        sentences = text_info.sentence_count

        if sentences < 1:
            return ReadingLevel.unknown

        all_difficult_words = set()
        for letter, letter_words in self._difficult_words().items():
            for word in letter_words:
                all_difficult_words.add(word.casefold())

        text_not_difficult_words = []
        text_difficult_words = []
        for word in text_info.words:
            if word.casefold() in all_difficult_words:
                text_difficult_words.append(word)
            else:
                text_not_difficult_words.append(word)

        difficult_words = len(text_difficult_words)

        result = 0.1579 * (difficult_words / words * 100.0) + 0.0496 * (words / sentences)
        if result < 3.5:  # this is made up
            level = ReadingLevel.grade_1
        elif result < 4.0:  # this is made up
            level = ReadingLevel.grade_2
        elif result < 4.5:  # this is made up
            level = ReadingLevel.grade_3
        elif result < 5.0:
            level = ReadingLevel.grade_4
        elif result < 5.5:  # this is made up
            level = ReadingLevel.grade_5
        elif result < 6.0:
            level = ReadingLevel.grade_6
        elif result < 6.5:  # this is made up
            level = ReadingLevel.grade_7
        elif result < 7.0:
            level = ReadingLevel.grade_8
        elif result < 7.5:  # this is made up
            level = ReadingLevel.grade_9
        elif result < 8.0:
            level = ReadingLevel.grade_10
        elif result < 8.5:  # this is made up
            level = ReadingLevel.grade_11
        elif result < 9.0:
            level = ReadingLevel.grade_12
        elif result < 9.33:  # this is made up
            level = ReadingLevel.grade_13
        elif result < 9.66:  # this is made up
            level = ReadingLevel.grade_14
        elif result < 10:
            level = ReadingLevel.grade_15
        elif result < 11:  # this is made up
            level = ReadingLevel.grade_16
        else:  # this is made up
            level = ReadingLevel.grade_17
        return level

    @staticmethod
    def _difficult_words():
        words = {
            "a": [
                "a", "able", "aboard", "about", "above", "absent", "accept", "accident", "account", "ache", "aching",
                "acorn", "acre", "across", "act", "acts", "add", "address", "admire", "adventure", "afar", "afraid",
                "after", "afternoon", "afterward", "afterwards", "again", "against", "age", "aged", "ago", "agree",
                "ah", "ahead", "aid", "aim", "air", "airfield", "airplane", "airport", "airship", "airy", "alarm",
                "alike", "alive", "all", "alley", "alligator", "allow", "almost", "alone", "along", "aloud", "already",
                "also", "always", "am", "America", "American", "among", "amount", "an", "and", "angel", "anger",
                "angry", "animal", "another", "answer", "ant", "any", "anybody", "anyhow", "anyone", "anything",
                "anyway", "anywhere", "apart", "apartment", "ape", "apiece", "appear", "apple", "April", "apron", "are",
                "aren't", "arise", "arithmetic", "arm", "armful", "army", "arose", "around", "arrange", "arrive",
                "arrived", "arrow", "art", "artist", "as", "ash", "ashes", "aside", "ask", "asleep", "at", "ate",
                "attack", "attend", "attention", "August", "aunt", "author", "auto", "automobile", "autumn", "avenue",
                "awake", "awaken", "away", "awful", "awfully", "awhile", "ax", "axe"
            ],
            "b": [
                "baa", "babe", "babies", "back", "background", "backward", "backwards", "bacon", "bad", "badge",
                "badly", "bag", "bake", "baker", "bakery", "baking", "ball", "balloon", "banana", "band", "bandage",
                "bang", "banjo", "bank", "banker", "bar", "barber", "bare", "barefoot", "barely", "bark", "barn",
                "barrel", "base", "baseball", "basement", "basket", "bat", "batch", "bath", "bathe", "bathing",
                "bathroom", "bathtub", "battle", "battleship", "bay", "be", "beach", "bead", "beam", "bean", "bear",
                "beard", "beast", "beat", "beating", "beautiful", "beautify", "beauty", "became", "because", "become",
                "becoming", "bed", "bedbug", "bedroom", "bedspread", "bedtime", "bee", "beech", "beef", "beefsteak",
                "beehive", "been", "beer", "beet", "before", "beg", "began", "beggar", "begged", "begin", "beginning",
                "begun", "behave", "behind", "being", "believe", "bell", "belong", "below", "belt", "bench", "bend",
                "beneath", "bent", "berries", "berry", "beside", "besides", "best", "bet", "better", "between", "bib",
                "bible", "bicycle", "bid", "big", "bigger", "bill", "billboard", "bin", "bind", "bird", "birth",
                "birthday", "biscuit", "bit", "bite", "biting", "bitter", "black", "blackberry", "blackbird",
                "blackboard", "blackness", "blacksmith", "blame", "blank", "blanket", "blast", "blaze", "bleed",
                "bless", "blessing", "blew", "blind", "blindfold", "blinds", "block", "blood", "bloom", "blossom",
                "blot", "blow", "blue", "blueberry", "bluebird", "blush", "board", "boast", "boat", "bob", "bobwhite",
                "bodies", "body", "boil", "boiler", "bold", "bone", "bonnet", "boo", "book", "bookcase", "bookkeeper",
                "boom", "boot", "born", "borrow", "boss", "both", "bother", "bottle", "bottom", "bought", "bounce",
                "bow", "bowl", "bow-wow", "box", "boxcar", "boxer", "boxes", "boy", "boyhood", "bracelet", "brain",
                "brake", "bran", "branch", "brass", "brave", "bread", "break", "breakfast", "breast", "breath",
                "breathe", "breeze", "brick", "bride", "bridge", "bright", "brightness", "bring", "broad", "broadcast",
                "broke", "broken", "brook", "broom", "brother", "brought", "brown", "brush", "bubble", "bucket",
                "buckle", "bud", "buffalo", "bug", "buggy", "build", "building", "built", "bulb", "bull", "bullet",
                "bum", "bumblebee", "bump", "bun", "bunch", "bundle", "bunny", "burn", "burst", "bury", "bus", "bush",
                "bushel", "business", "busy", "but", "butcher", "butt", "butter", "buttercup", "butterfly",
                "buttermilk", "butterscotch", "button", "buttonhole", "buy", "buzz", "by", "bye"
            ],
            "c": [
                "cab", "cabbage", "cabin", "cabinet", "cackle", "cage", "cake", "calendar", "calf", "call", "caller",
                "calling", "came", "camel", "camp", "campfire", "can", "canal", "canary", "candle", "candlestick",
                "candy", "cane", "cannon", "cannot", "canoe", "can't", "canyon", "cap", "cape", "capital", "captain",
                "car", "card", "cardboard", "care", "careful", "careless", "carelessness", "carload", "carpenter",
                "carpet", "carriage", "carrot", "carry", "cart", "carve", "case", "cash", "cashier", "castle", "cat",
                "catbird", "catch", "catcher", "caterpillar", "catfish", "catsup", "cattle", "caught", "cause", "cave",
                "ceiling", "cell", "cellar", "cent", "center", "cereal", "certain", "certainly", "chain", "chair",
                "chalk", "champion", "chance", "change", "chap", "charge", "charm", "chart", "chase", "chatter",
                "cheap", "cheat", "check", "checkers", "cheek", "cheer", "cheese", "cherry", "chest", "chew", "chick",
                "chicken", "chief", "child", "childhood", "children", "chill", "chilly", "chimney", "chin", "china",
                "chip", "chipmunk", "chocolate", "choice", "choose", "chop", "chorus", "chose", "chosen", "christen",
                "Christmas", "church", "churn", "cigarette", "circle", "circus", "citizen", "city", "clang", "clap",
                "class", "classmate", "classroom", "claw", "clay", "clean", "cleaner", "clear", "clerk", "clever",
                "click", "cliff", "climb", "clip", "cloak", "clock", "close", "closet", "cloth", "clothes", "clothing",
                "cloud", "cloudy", "clover", "clown", "club", "cluck", "clump", "coach", "coal", "coast", "coat", "cob",
                "cobbler", "cocoa", "coconut", "cocoon", "cod", "codfish", "coffee", "coffeepot", "coin", "cold",
                "collar", "college", "color", "colored", "colt", "column", "comb", "come", "comfort", "comic", "coming",
                "company", "compare", "conductor", "cone", "connect", "coo", "cook", "cooked", "cooking", "cookie",
                "cookies", "cool", "cooler", "coop", "copper", "copy", "cord", "cork", "corn", "corner", "correct",
                "cost", "cot", "cottage", "cotton", "couch", "cough", "could", "couldn't", "count", "counter",
                "country", "county", "course", "court", "cousin", "cover", "cow", "coward", "cowardly", "cowboy",
                "cozy", "crab", "crack", "cracker", "cradle", "cramps", "cranberry", "crank", "cranky", "crash",
                "crawl", "crazy", "cream", "creamy", "creek", "creep", "crept", "cried", "croak", "crook", "crooked",
                "crop", "cross", "crossing", "cross-eyed", "crow", "crowd", "crowded", "crown", "cruel", "crumb",
                "crumble", "crush", "crust", "cry", "cries", "cub", "cuff", "cup", "cuff", "cup", "cupboard", "cupful",
                "cure", "curl", "curly", "curtain", "curve", "cushion", "custard", "customer", "cut", "cute", "cutting",
            ],
            "d": [
                "dab", "dad", "daddy", "daily", "dairy", "daisy", "dam", "damage", "dame", "damp", "dance", "dancer",
                "dancing", "dandy", "danger", "dangerous", "dare", "dark", "darkness", "darling", "darn", "dart",
                "dash", "date", "daughter", "dawn", "day", "daybreak", "daytime", "dead", "deaf", "deal", "dear",
                "death", "December", "decide", "deck", "deed", "deep", "deer", "defeat", "defend", "defense", "delight",
                "den", "dentist", "depend", "deposit", "describe", "desert", "deserve", "desire", "desk", "destroy",
                "devil", "dew", "diamond", "did", "didn't", "die", "died", "dies", "difference", "different", "dig",
                "dim", "dime", "dine", "ding-dong", "dinner", "dip", "direct", "direction", "dirt",
                "dirty", "discover", "dish", "dislike", "dismiss", "ditch", "dive", "diver", "divide", "do", "dock",
                "doctor", "does", "doesn't", "dog", "doll", "dollar", "dolly", "done", "donkey", "don't", "door",
                "doorbell", "doorknob", "doorstep", "dope", "dot", "double", "dough", "dove", "down", "downstairs",
                "downtown", "dozen", "drag", "drain", "drank", "draw", "drawer", "draw", "drawing", "dream", "dress",
                "dresser", "dressmaker", "drew", "dried", "drift", "drill", "drink", "drip", "drive", "driven",
                "driver", "drop", "drove", "drown", "drowsy", "drub", "drum", "drunk", "dry", "duck", "due", "dug",
                "dull", "dumb", "dump", "during", "dust", "dusty", "duty", "dwarf", "dwell", "dwelt", "dying",
            ],
            "e": [
                "each", "eager", "eagle", "ear", "early", "earn", "earth", "east", "eastern", "easy", "eat",
                "eaten", "edge", "egg", "eh", "eight", "eighteen", "eighth", "eighty", "either", "elbow", "elder",
                "eldest", "electric", "electricity", "elephant", "eleven", "elf", "elm", "else", "elsewhere", "empty",
                "end", "ending", "enemy", "engine", "engineer", "English", "enjoy", "enough", "enter", "envelope",
                "equal", "erase", "eraser", "errand", "escape", "eve", "even", "evening", "ever", "every", "everybody",
                "everyday", "everyone", "everything", "everywhere", "evil", "exact", "except", "exchange", "excited",
                "exciting", "excuse", "exit", "expect", "explain", "extra", "eye", "eyebrow",
            ],
            "f": [

                "fable", "face", "facing", "fact", "factory", "fail", "faint", "fair", "fairy", "faith", "fake", "fall",
                "false", "family", "fan", "fancy", "far", "faraway", "fare", "farmer", "farm", "farming", "far-off",
                "farther", "fashion", "fast", "fasten", "fat", "father", "fault", "favor", "favorite", "fear", "feast",
                "feather", "February", "fed", "feed", "feel", "feet", "fell", "fellow", "felt", "fence", "fever", "few",
                "fib", "fiddle", "field", "fife", "fifteen", "fifth", "fifty", "fig", "fight", "figure", "file",
                "fill", "film", "finally", "find", "fine", "finger", "finish", "fire", "firearm", "firecracker",
                "fireplace", "fireworks", "firing", "first", "fish", "fisherman", "fist", "fit", "fits", "five", "fix",
                "flag", "flake", "flame", "flap", "flash", "flashlight", "flat", "flea", "flesh", "flew", "flies",
                "flight", "flip", "flip-flop", "float", "flock", "flood", "floor", "flop", "flour", "flow", "flower",
                "flowery", "flutter", "fly", "foam", "fog", "foggy", "fold", "folks", "follow", "following", "fond",
                "food", "fool", "foolish", "foot", "football", "footprint", "for", "forehead", "forest", "forget",
                "forgive", "forgot", "forgotten", "fork", "form", "fort", "forth", "fortune", "forty", "forward",
                "fought", "found", "fountain", "four", "fourteen", "fourth", "fox", "frame", "free", "freedom",
                "freeze", "freight", "French", "fresh", "fret", "Friday", "fried", "friend", "friendly", "friendship",
                "frighten", "frog", "from", "front", "frost", "frown", "froze", "fruit", "fry", "fudge", "fuel", "full",
                "fully", "fun", "funny", "fur", "furniture", "further", "fuzzy",
            ],
            "g": [

                "gain", "gallon", "gallop", "game", "gang", "garage", "garbage", "garden", "gas", "gasoline", "gate",
                "gather", "gave", "gay", "gear", "geese", "general", "gentle", "gentleman", "gentlemen", "geography",
                "get", "getting", "giant", "gift", "gingerbread", "girl", "give", "given", "giving", "glad", "gladly",
                "glance", "glass", "glasses", "gleam", "glide", "glory", "glove", "glow", "glue", "go", "going",
                "goes", "goal", "goat", "gobble", "God", "god", "godmother", "gold", "golden", "goldfish", "golf",
                "gone", "good", "goods", "goodbye", "good-by", "goodbye", "good-bye", "good-looking", "goodness",
                "goody", "goose", "gooseberry", "got", "govern", "government", "gown", "grab", "gracious", "grade",
                "grain", "grand", "grandchild", "grandchildren", "granddaughter", "grandfather",
                "grandma", "grandmother", "grandpa", "grandson", "grandstand", "grape", "grapes", "grapefruit",
                "grass", "grasshopper", "grateful", "grave", "gravel", "graveyard", "gravy", "gray", "graze", "grease",
                "great", "green", "greet", "grew", "grind", "groan", "grocery", "ground", "group", "grove", "grow",
                "guard", "guess", "guest", "guide", "gulf", "gum", "gun", "gunpowder", "guy",
            ],
            "h": [
                "ha", "habit", "had", "hadn't", "hail", "hair", "haircut", "hairpin", "half", "hall", "halt", "ham",
                "hammer", "hand", "handful", "handkerchief", "handle", "handwriting", "hang", "happen", "happily",
                "happiness", "happy", "harbor", "hard", "hardly", "hardship", "hardware", "hare", "hark", "harm",
                "harness", "harp", "harvest", "has", "hasn't", "haste", "hasten", "hasty", "hat", "hatch", "hatchet",
                "hate", "haul", "have", "haven't", "having", "hawk", "hay", "hayfield", "haystack", "he", "head",
                "headache", "heal", "health", "healthy", "heap", "hear", "hearing", "heard", "heart", "heat", "heater",
                "heaven", "heavy", "he'd", "heel", "height", "held", "hell", "he'll", "hello", "helmet", "help",
                "helper", "helpful", "hem", "hen", "henhouse", "her", "hers", "herd", "here", "here's", "hero",
                "herself", "he's", "hey", "hickory", "hid", "hidden", "hide", "high", "highway", "hill", "hillside",
                "hilltop", "hilly", "him", "himself", "hind", "hint", "hip", "hire", "his", "hiss", "history", "hit",
                "hitch", "hive", "ho", "hoe", "hog", "hold", "holder", "hole", "holiday", "hollow", "holy", "home",
                "homely", "homesick", "honest", "honey", "honeybee", "honeymoon", "honk", "honor", "hood", "hoof",
                "hook", "hoop", "hop", "hope", "hopeful", "hopeless", "horn", "horse", "horseback", "horseshoe", "hose",
                "hospital", "host", "hot", "hotel", "hound", "hour", "house", "housetop", "housewife", "housework",
                "how", "however", "howl", "hug", "huge", "hum", "humble", "hump", "hundred", "hung", "hunger", "hungry",
                "hunk", "hunt", "hunter", "hurrah", "hurried", "hurry", "hurt", "husband", "hush", "hut", "hymn",
            ],
            "i": [
                "I", "I", "ice", "icy", "I'd", "idea", "ideal", "if", "ill", "I'll", "I'm", "important", "impossible",
                "improve", "in", "inch", "inches", "income", "indeed", "Indian", "indoors", "ink", "inn", "insect",
                "inside", "instant", "instead", "insult", "intend", "interested", "interesting", "into",
                "invite", "iron", "is", "island", "isn't", "it", "its", "it's", "itself", "I've", "ivory", "ivy",
            ],
            "j": [
                "jacket", "jacks", "jail", "jam", "January", "jar", "jaw", "jay", "jelly", "jellyfish", "jerk",
                "jig", "job", "jockey", "join", "joke", "joking", "jolly", "journey", "joy", "joyful", "joyous",
                "judge", "jug", "juice", "juicy", "July", "jump", "June", "junior", "junk", "just",
            ],
            "k": [
                "keen", "keep", "kept", "kettle", "key", "kick", "kid", "kill", "killed", "kind", "kindly",
                "kindness", "king", "kingdom", "kiss", "kitchen", "kite", "kitten", "kitty", "knee", "kneel", "knew",
                "knife", "knit", "knives", "knob", "knock", "knot", "know", "known",
            ],
            "l": [
                "lace", "lad", "ladder", "ladies", "lady", "laid", "lake", "lamb", "lame", "lamp", "land", "lane",
                "language", "lantern", "lap", "lard", "large", "lash", "lass", "last", "late", "laugh", "laundry",
                "law", "lawn", "lawyer", "lay", "lazy", "lead", "leader", "leaf", "leak", "lean", "leap", "learn",
                "learned", "least", "leather", "leave", "leaving", "led", "left", "leg", "lemon", "lemonade", "lend",
                "length", "less", "lesson", "let", "let's", "letter", "letting", "lettuce", "level", "liberty",
                "library", "lice", "lick", "lid", "lie", "life", "lift", "light", "lightness", "lightning", "like",
                "likely", "liking", "lily", "limb", "lime", "limp", "line", "linen", "lion", "lip", "list", "listen",
                "lit", "little", "live", "lives", "lively", "liver", "living", "lizard", "load", "loaf", "loan",
                "loaves", "lock", "locomotive", "log", "lone", "lonely", "lonesome", "long", "look", "lookout", "loop",
                "loose", "lord", "lose", "loser", "loss", "lost", "lot", "loud", "love", "lovely", "lover", "low",
                "luck", "lucky", "lumber", "lump", "lunch", "lying",
            ],
            "m": [
                "ma", "machine", "machinery", "mad", "made", "magazine", "magic", "maid", "mail", "mailbox", "mailman",
                "major", "make", "making", "male", "mama", "mamma", "man", "manager", "mane", "manger", "many",
                "map", "maple", "marble", "march", "March", "mare", "mark", "market", "marriage", "married", "marry",
                "mask", "mast", "master", "mat", "match", "matter", "mattress", "may", "May", "maybe", "mayor",
                "maypole", "me", "meadow", "meal", "mean", "means", "meant", "measure", "meat", "medicine", "meet",
                "meeting", "melt", "member", "men", "mend", "meow", "merry", "mess", "message", "met", "metal", "mew",
                "mice", "middle", "midnight", "might", "mighty", "mile", "milk", "milkman", "mill", "miler", "million",
                "mind", "mine", "miner", "mint", "minute", "mirror", "mischief", "miss", "Miss", "misspell", "mistake",
                "misty", "mitt", "mitten", "mix", "moment", "Monday", "money", "monkey", "month", "moo", "moon",
                "moonlight", "moose", "mop", "more", "morning", "morrow", "moss", "most", "mostly", "mother", "motor",
                "mount", "mountain", "mouse", "mouth", "move", "movie", "movies", "moving", "mow", "Mr.", "Mrs.",
                "much", "mud", "muddy", "mug", "mule", "multiply", "murder", "music", "must", "my", "myself",
            ],
            "n": [

                "nail", "name", "nap", "napkin", "narrow", "nasty", "naughty", "navy", "near", "nearby", "nearly",
                "neat", "neck", "necktie", "need", "needle", "needn't", "Negro", "neighbor", "neighborhood", "neither",
                "nerve", "nest", "net", "never", "nevermore", "new", "news", "newspaper", "next", "nibble", "nice",
                "nickel", "night", "nightgown", "nine", "nineteen", "ninety", "no", "nobody", "nod", "noise", "noisy",
                "none", "noon", "nor", "north", "northern", "nose", "not", "note", "nothing", "notice", "November",
                "now", "nowhere", "number", "nurse", "nut",
            ],
            "o": [
                "oak", "oar", "oatmeal", "oats", "obey", "ocean", "o'clock", "October", "odd", "of", "off", "offer",
                "office", "officer", "often", "oh", "oil", "old", "old-fashioned", "on", "once", "one", "onion",
                "only", "onward", "open", "or", "orange", "orchard", "order", "ore", "organ", "other", "otherwise",
                "ouch", "ought", "our", "ours", "ourselves", "out", "outdoors", "outfit", "outlaw",
                "outline", "outside", "outward", "oven", "over", "overalls", "overcoat", "overeat", "overhead",
                "overhear", "overnight", "overturn", "owe", "owing", "owl", "own", "owner", "ox",
            ],
            "p": [
                "pa", "pace", "pack", "package", "pad", "page", "paid", "pail", "pain", "painful", "paint", "painter",
                "painting", "pair", "pal", "palace", "pale", "pan", "pancake", "pane", "pansy", "pants", "papa",
                "paper", "parade", "pardon", "parent", "park", "part", "partly", "partner", "party", "pass",
                "passenger", "past", "paste", "pasture", "pat", "patch", "path", "patter", "pave", "pavement", "paw",
                "pay", "payment", "pea", "peas", "peace", "peaceful", "peach", "peaches", "peak", "peanut", "pear",
                "pearl", "peck", "peek", "peel", "peep", "peg", "pen", "pencil", "penny", "people", "pepper",
                "peppermint", "perfume", "perhaps", "person", "pet", "phone", "piano", "pick", "pickle", "picnic",
                "picture", "pie", "piece", "pig", "pigeon", "piggy", "pile", "pill", "pillow", "pin", "pine",
                "pineapple", "pink", "pint", "pipe", "pistol", "pit", "pitch", "pitcher", "pity", "place", "plain",
                "plan", "plane", "plant", "plate", "platform", "platter", "play", "player", "playground", "playhouse",
                "playmate", "plaything", "pleasant", "please", "pleasure", "plenty", "plow", "plug", "plum", "pocket",
                "pocketbook", "poem", "point", "poison", "poke", "pole", "police", "policeman", "polish",
                "polite", "pond", "ponies", "pony", "pool", "poor", "pop", "popcorn", "popped", "porch", "pork",
                "possible", "post", "postage", "postman", "pot", "potato", "potatoes", "pound", "pour", "powder",
                "power", "powerful", "praise", "pray", "prayer", "prepare", "present", "pretty", "price", "prick",
                "prince", "princess", "print", "prison", "prize", "promise", "proper", "protect", "proud", "prove",
                "prune", "public", "puddle", "puff", "pull", "pump", "pumpkin", "punch", "punish", "pup", "pupil",
                "puppy", "pure", "purple", "purse", "push", "puss", "pussy", "pussycat", "put", "putting", "puzzle",
            ],
            "q": [
                "quack", "quart", "quarter", "queen", "queer", "question", "quick", "quickly", "quiet",
                "quilt", "quit", "quite",
            ],
            "r": [
                "rabbit", "race", "rack", "radio", "radish", "rag", "rail", "railroad", "railway", "rain", "rainy",
                "rainbow", "raise", "raisin", "rake", "ram", "ran", "ranch", "rang", "rap", "rapidly", "rat", "rate",
                "rather", "rattle", "raw", "ray", "reach", "read", "reader", "reading", "ready", "real", "really",
                "reap", "rear", "reason", "rebuild", "receive", "recess", "record", "red", "redbird", "redbreast",
                "refuse", "reindeer", "rejoice", "remain", "remember", "remind", "remove", "rent", "repair", "repay",
                "repeat", "report", "rest", "return", "review", "reward", "rib", "ribbon", "rice", "rich", "rid",
                "riddle", "ride", "rider", "riding", "right", "rim", "ring", "rip", "ripe", "rise", "rising", "river",
                "road", "roadside", "roar", "roast", "rob", "robber", "robe", "robin", "rock", "rocky", "rocket",
                "rode", "roll", "roller", "roof", "room", "rooster", "root", "rope", "rose", "rosebud", "rot", "rotten",
                "rough", "round", "route", "row", "rowboat", "royal", "rub", "rubbed", "rubber", "rubbish", "rug",
                "rule", "ruler", "rumble", "run", "rung", "runner", "running", "rush", "rust", "rusty", "rye",
            ],
            "s": [
                "sack", "sad", "saddle", "sadness", "safe", "safety", "said", "sail", "sailboat", "sailor", "saint",
                "salad", "sale", "salt", "same", "sand", "sandy", "sandwich", "sang", "sank", "sap", "sash", "sat",
                "satin", "satisfactory", "Saturday", "sausage", "savage", "save", "savings", "saw", "say", "scab",
                "scales", "scare", "scarf", "school", "schoolboy", "schoolhouse", "schoolmaster", "schoolroom",
                "scorch", "score", "scrap", "scrape", "scratch", "scream", "screen", "screw", "scrub", "sea", "seal",
                "seam", "search", "season", "seat", "second", "secret", "see", "seeing", "seed", "seek", "seem", "seen",
                "seesaw", "select", "self", "selfish", "sell", "send", "sense", "sent", "sentence", "separate",
                "September", "servant", "serve", "service", "set", "setting", "settle", "settlement", "seven",
                "seventeen", "seventh", "seventy", "several", "sew", "shade", "shadow", "shady", "shake", "shaker",
                "shaking", "shall", "shame", "shan't", "shape", "share", "sharp", "shave", "she", "she'd", "she'll",
                "she's", "shear", "shears", "shed", "sheep", "sheet", "shelf", "shell", "shepherd", "shine", "shining",
                "shiny", "ship", "shirt", "shock", "shoe", "shoemaker", "shone", "shook", "shoot", "shop", "shopping",
                "shore", "short", "shot", "should", "shoulder", "shouldn't", "shout", "shovel", "show",
                "shower", "shut", "shy", "sick", "sickness", "side", "sidewalk", "sideways", "sigh", "sight", "sign",
                "silence", "silent", "silk", "sill", "silly", "silver", "simple", "sin", "since", "sing", "singer",
                "single", "sink", "sip", "sir", "sis", "sissy", "sister", "sit", "sitting", "six", "sixteen", "sixth",
                "sixty", "size", "skate", "skater", "ski", "skin", "skip", "skirt", "sky", "slam", "slap", "slate",
                "slave", "sled", "sleep", "sleepy", "sleeve", "sleigh", "slept", "slice", "slid", "slide", "sling",
                "slip", "slipped", "slipper", "slippery", "slit", "slow", "slowly", "sly", "smack", "small", "smart",
                "smell", "smile", "smoke", "smooth", "snail", "snake", "snap", "snapping", "sneeze", "snow", "snowy",
                "snowball", "snowflake", "snuff", "snug", "so", "soak", "soap", "sob", "socks", "sod", "soda", "sofa",
                "soft", "soil", "sold", "soldier", "sole", "some", "somebody", "somehow", "someone", "something",
                "sometime", "sometimes", "somewhere", "son", "song", "soon", "sore", "sorrow", "sorry", "sort", "soul",
                "sound", "soup", "sour", "south", "southern", "space", "spade", "spank", "sparrow", "speak", "speaker",
                "spear", "speech", "speed", "spell", "spelling", "spend", "spent", "spider", "spike", "spill", "spin",
                "spinach", "spirit", "spit", "splash", "spoil", "spoke", "spook", "spoon", "sport", "spot", "spread",
                "spring", "springtime", "sprinkle", "square", "squash", "squeak", "squeeze", "squirrel", "stable",
                "stack", "stage", "stair", "stall", "stamp", "stand", "star", "stare", "start", "starve", "state",
                "station", "stay", "steak", "steal", "steam", "steamboat", "steamer", "steel", "steep", "steeple",
                "steer", "stem", "step", "stepping", "stick", "sticky", "stiff", "still", "stillness", "sting", "stir",
                "stitch", "stock", "stocking", "stole", "stone", "stood", "stool", "stoop", "stop", "stopped",
                "stopping", "store", "stork", "stories", "storm", "stormy", "story", "stove", "straight", "strange",
                "stranger", "strap", "straw", "strawberry", "stream", "street", "stretch", "string", "strip", "stripes",
                "strong", "stuck", "study", "stuff", "stump", "stung", "subject", "such", "suck", "sudden", "suffer",
                "sugar", "suit", "sum", "summer", "sun", "Sunday", "sunflower", "sung", "sunk", "sunlight", "sunny",
                "sunrise", "sunset", "sunshine", "supper", "suppose", "sure", "surely", "surface", "surprise",
                "swallow", "swam", "swamp", "swan", "swat", "swear", "sweat", "sweater", "sweep", "sweet", "sweetness",
                "sweetheart", "swell", "swept", "swift", "swim", "swimming", "swing", "switch", "sword", "swore",
            ],
            "t": [
                "table", "tablecloth", "tablespoon", "tablet", "tack", "tag", "tail", "tailor", "take", "taken",
                "taking", "tale", "talk", "talker", "tall", "tame", "tan", "tank", "tap", "tape", "tar", "tardy",
                "task", "taste", "taught", "tax", "tea", "teach", "teacher", "team", "tear", "tease", "teaspoon",
                "teeth", "telephone", "tell", "temper", "ten", "tennis", "tent", "term", "terrible", "test", "than",
                "thank", "thanks", "thankful", "Thanksgiving", "that", "that's", "the", "theater", "thee", "their",
                "them", "then", "there", "these", "they", "they'd", "they'll", "they're", "they've", "thick", "thief",
                "thimble", "thin", "thing", "think", "third", "thirsty", "thirteen", "thirty", "this", "thorn", "those",
                "though", "thought", "thousand", "thread", "three", "threw", "throat", "throne", "through", "throw",
                "thrown", "thumb", "thunder", "Thursday", "thy", "tick", "ticket", "tickle", "tie", "tiger", "tight",
                "till", "time", "tin", "tinkle", "tiny", "tip", "tiptoe", "tire", "tired", "title", "to", "toad",
                "toadstool", "toast", "tobacco", "today", "toe", "together", "toilet", "told", "tomato", "tomorrow",
                "ton", "tone", "tongue", "tonight", "too", "took", "tool", "toot", "tooth", "toothbrush", "toothpick",
                "top", "tore", "torn", "toss", "touch", "tow", "toward", "towards", "towel", "tower", "town", "toy",
                "trace", "track", "trade", "train", "tramp", "trap", "tray", "treasure", "treat", "tree", "trick",
                "tricycle", "tried", "trim", "trip", "trolley", "trouble", "truck", "true", "truly", "trunk", "trust",
                "truth", "try", "tub", "Tuesday", "tug", "tulip", "tumble", "tune", "tunnel", "turkey", "turn",
                "turtle", "twelve", "twenty", "twice", "twig", "twin", "two",
            ],
            "u": [
                "ugly", "umbrella", "uncle", "under", "understand", "underwear", "undress", "unfair", "unfinished",
                "unfold", "unfriendly", "unhappy", "unhurt", "uniform", "United", "States", "unkind",
                "unknown", "unless", "unpleasant", "until", "unwilling", "up", "upon", "upper", "upset", "upside",
                "upstairs", "uptown", "upward", "us", "use", "used", "useful",
            ],
            "v": [
                "valentine", "valley", "valuable", "value", "vase", "vegetable", "velvet", "very",
                "vessel", "victory", "view", "village", "vine", "violet", "visit", "visitor", "voice", "vote",
            ],
            "w": [
                "wag", "wagon", "waist", "wait", "wake", "waken", "walk", "wall", "walnut", "want", "war", "warm",
                "warn", "was", "wash", "washer", "washtub", "wasn't", "waste", "watch", "watchman", "water",
                "watermelon", "waterproof", "wave", "wax", "way", "wayside", "we", "weak", "weakness", "weaken",
                "wealth", "weapon", "wear", "weary", "weather", "weave", "web", "we'd", "wedding", "Wednesday", "wee",
                "weed", "week", "we'll", "weep", "weigh", "welcome", "well", "went", "were", "we're", "west",
                "western", "wet", "we've", "whale", "what", "what's", "wheat", "wheel", "when", "whenever", "where",
                "which", "while", "whip", "whipped", "whirl", "whisky", "whiskey", "whisper", "whistle", "white", "who",
                "who'd", "whole", "who'll", "whom", "who's", "whose", "why", "wicked", "wide", "wife", "wiggle",
                "wild", "wildcat", "will", "willing", "willow", "win", "wind", "windy", "windmill", "window", "wine",
                "wing", "wink", "winner", "winter", "wipe", "wire", "wise", "wish", "wit", "witch", "with", "without",
                "woke", "wolf", "woman", "women", "won", "wonder", "wonderful", "won't", "wood", "wooden", "woodpecker",
                "woods", "wool", "woolen", "word", "wore", "work", "worker", "workman", "world", "worm", "worn",
                "worry", "worse", "worst", "worth", "would", "wouldn't", "wound", "wove", "wrap", "wrapped", "wreck",
                "wren", "wring", "write", "writing", "written", "wrong", "wrote", "wrung",
            ],
            "x": [
            ],
            "y": [
                "yard", "yarn", "year", "yell", "yellow", "yes", "yesterday", "yet", "yolk", "yonder", "you",
                "you'd", "you'll", "young", "youngster", "your", "yours", "you're", "yourself",
                "yourselves", "youth", "you've",
            ],
            "z": [
            ]
        }
        return words
