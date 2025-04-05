import random
difficulty_title_dict = {
        "easy": ["Albert Einstein", "Marie Curie", "Isaac Newton", "Charles Darwin", "Leonardo da Vinci",
              "Galileo Galilei", "Thomas Edison", "Gebrüder Grimm", "Wolfgang Amadeus Mozart",
              "Ludwig van Beethoven", "Johann Sebastian Bach", "Vincent van Gogh", "Pablo Picasso",
              "Christoph Kolumbus", "Neil Armstrong",
              "Martin Luther King Jr.", "Mahatma Gandhi", "Nelson Mandela", "Anne Frank", "Albert Schweitzer",
              "Mutter Teresa", "Karl der Große", "Jeanne d’Arc", "Kleopatra", "Julius Cäsar", "Alexander der Große",
              "König Artus", "Robin Hood", "Buddha", "Jesus Christus", "Mohammed", "Mose", "David", "Salomo", "Homer",
              "Elvis Presley", "The Beatles", "Michael Jackson", "Charlie Chaplin", "Walt Disney", "Mickey Mouse",
              "Donald Duck", "Pippi Langstrumpf", "Harry Potter", "Schneewittchen", "Aschenputtel", "Rotkäppchen",
              "Dornröschen", "Hänsel und Gretel", "Till Eulenspiegel", "Max und Moritz", "Heidi", "Pinocchio",
              "Peter Pan", "Mowgli", "Winnie Puuh", "Paddington Bär", "Die Biene Maja", "Benjamin Blümchen",
              "Bibi Blocksberg", "Lassie", "Pluto", "Goofy", "Dagobert Duck", "Tick Trick Track", "Olaf", "Elsa",
              "Anna", "SpongeBob Schwammkopf", "Patrick Star", "Arielle", "Simba", "Nala", "Timon", "Pumbaa", "Balu",
              "Mogli", "Bambi", "Dumbo", "Rapunzel", "Cinderella", "Die Bremer Stadtmusikanten",
              "Der gestiefelte Kater", "Frau Holle", "Rumpelstilzchen", "Die Prinzessin auf der Erbse",
              "Der Froschkönig", "Die kleine Meerjungfrau", "Die Schneekönigin", "Die wilden Schwäne",
              "Des Kaisers neue Kleider", "Der standhafte Zinnsoldat", "Das hässliche Entlein", "Die Nachtigall",
              "Die Regentrude", "Der kleine Muck", "Kalif Storch", "Das kalte Herz",
              "Die Geschichte vom kleinen Maulwurf, der wissen wollte, wer ihm auf den Kopf gemacht hat",
              "Die Raupe Nimmersatt", "Der Regenbogenfisch", "Frederick", "Swimmy", "Kleiner Eisbär, wohin fährst du?",
              "Die Geschichte vom Löwen, der nicht schreiben konnte", "Die Olchis", "Das kleine Gespenst",
              "Der Räuber Hotzenplotz", "Das Sams", "Jim Knopf und Lukas der Lokomotivführer", "Momo",
              "Die unendliche Geschichte", "Ronja Räubertochter", "Michel aus Lönneberga", "Madita",
              "Karlsson vom Dach", "Die Brüder Löwenherz", "Wir Kinder aus Bullerbü", "Der kleine Prinz",
              "Der Zauberer von Oz", "Alice im Wunderland", "Peter Hase", "Flipper", "Fury", "Black Beauty",
              "Der kleine Vampir", "Hexe Lilli", "Die Schule der magischen Tiere", "Gregs Tagebuch",
              "Das magische Baumhaus", "Die drei ???", "TKKG", "Fünf Freunde", "Hanni und Nanni", "Die wilden Hühner"],
        "normal": ["Stephen Hawking", "Nikola Tesla", "Alan Turing", "Ada Lovelace", "Rosalind Franklin",
              "William Shakespeare", "Johann Wolfgang von Goethe", "Charles Dickens", "Frida Kahlo",
              "Michelangelo", "Claude Monet", "J.K. Rowling", "Napoleon Bonaparte", "Winston Churchill",
              "Abraham Lincoln", "George Washington", "Friedrich der Große", "Otto von Bismarck", "Angela Merkel",
              "Muhammad Ali", "Michael Jordan", "Usain Bolt", "Serena Williams", "Lionel Messi", "Cristiano Ronaldo",
              "Michael Schumacher", "Steffi Graf", "Dirk Nowitzki", "Franz Beckenbauer",
              "Madonna", "Freddie Mercury", "David Bowie", "Beyoncé",
              "Marilyn Monroe", "Steven Spielberg", "Tom Hanks", "Meryl Streep",
              "Daniel Radcliffe", "Platon", "Aristoteles", "Konfuzius", "Martin Luther", "Ferdinand Magellan",
              "Roald Amundsen", "Yuri Gagarin", "Jacques Cousteau", "Steve Irwin", "Malala Yousafzai",
              "Oskar Schindler", "Sophie Scholl", "Dietrich Bonhoeffer", "Clara Zetkin", "Che Guevara", "Desmond Tutu",
              "Dalai Lama", "Alfred Nobel", "Florence Nightingale", "Henry Ford", "Coco Chanel", "Steve Jobs",
              "Bill Gates", "Jeff Bezos", "Mark Zuckerberg", "Elon Musk", "Konrad Adenauer", "Willy Brandt",
              "Marlene Dietrich", "Heidi Klum", "Til Schweiger", "Bastian Schweinsteiger", "Manuel Neuer", "Mesut Özil",
              "Thomas Müller", "Karl Lagerfeld", "Sigmund Freud", "Arnold Schwarzenegger", "Falco", "Niki Lauda",
              "Christoph Waltz", "Roger Federer", "Martina Hingis", "Albert Hofmann", "Le Corbusier",
              "Friedrich Dürrenmatt", "Leonardo DiCaprio", "Angelina Jolie", "Brad Pitt", "Lady Gaga", "Rihanna",
              "Dwayne 'The Rock' Johnson", "Keanu Reeves", "Jackie Chan", "Bruce Lee", "Jackie Kennedy", "Ramses II.",
              "Hannibal", "Attila der Hunne", "Dschingis Khan", "Vasco da Gama", "Hernán Cortés", "Francisco Pizarro",
              "William der Eroberer", "Richard Löwenherz", "Achilles", "Tutanchamun", "Vergil", "Dante Alighieri",
              "Geoffrey Chaucer", "Miguel de Cervantes", "Rembrandt", "Johannes Gutenberg", "William Harvey",
              "René Descartes", "Blaise Pascal", "Robert Boyle", "Anton van Leeuwenhoek", "Carl von Linné",
              "Benjamin Franklin", "James Watt",
              "André-Marie Ampère", "Michael Faraday", "Joseph Henry", "Samuel Morse", "Louis Daguerre",
              "Gregor Mendel", "Alexander Fleming", "Francis Crick",
              "Stephenie Meyer", "Suzanne Collins", "J.R.R. Tolkien", "George Orwell", "Agatha Christie",
              "Ernest Hemingway", "Mark Twain", "Edgar Allan Poe", "Karl Marx",
              "Friedrich Nietzsche", "Max Planck", "Lise Meitner", "Erich Maria Remarque",
              "Thomas Mann", "Bertolt Brecht", "Franz Kafka", "Heinrich Heine", "Stefan Zweig", "Gustav Klimt",
              "Jean-Jacques Rousseau", "Carl Gustav Jung", "Patricia Highsmith", "Thomas Jefferson", "John F. Kennedy",
              "Maya Angelou", "Nofretete", "Simón Bolívar", "David Unaipon", "Taylor Swift",
              "Billie Eilish", "Ariana Grande", "Justin Bieber", "Shakira", "Drake", "Eminem", "Snoop Dogg", "Jay-Z",
              "Kim Kardashian", "Kylie Jenner", "Travis Scott", "Zendaya", "Timothée Chalamet", "Anya Taylor-Joy",
              "Jenna Ortega", "Pedro Pascal", "Margot Robbie", "David Beckham", "Tom Brady", "Lewis Hamilton",
              "Tiger Woods", "Michael Phelps", "Simone Biles" "Naomi Osaka", "Coco Gauff",
              "Rafael Nadal", "Novak Djokovic", "Maria Sharapova"],
        "hard": [
             "Johannes Kepler", "Niels Bohr", "Werner Heisenberg", "Richard Feynman", "Erwin Schrödinger",
             "Enrico Fermi", "James Clerk Maxwell", "Ernest Rutherford", "Antoine Lavoisier",
             "Dmitri Mendeleev", "Jonas Salk", "James Watson",
             "Louis Pasteur", "Alexander von Humboldt", "Carl Friedrich Gauß", "Leonhard Euler", "Bernhard Riemann",
             "David Hilbert", "Emmy Noether", "Kurt Gödel", "John von Neumann", "Claude Shannon", "Andrei Kolmogorov",
             "Norbert Wiener", "Grace Hopper", "Edsger W. Dijkstra", "Donald Knuth", "Tim Berners-Lee", "Linus Pauling",
             "Dorothy Hodgkin", "Barbara McClintock", "Rachel Carson", "Jane Goodall", "Stephen Jay Gould",
             "Edward O. Wilson", "Carl Sagan", "Neil deGrasse Tyson", "Michio Kaku", "Brian Greene", "Lisa Randall",
             "Sabine Hossenfelder", "Sean M. Carroll", "Lawrence M. Krauss", "Sheldon Glashow", "Steven Weinberg",
             "Abdus Salam", "Murray Gell-Mann", "Richard E. Smalley", "Robert Curl", "Harold Kroto", "Kary Mullis",
             "Jennifer Doudna", "Emmanuelle Charpentier", "Craig Venter", "Francis Collins", "Eric Lander",
             "Svante Pääbo", "David Baltimore", "Howard Temin", "Joshua Lederberg", "Stanley Prusiner",
             "Elizabeth Blackburn", "Carol Greider", "Jack Szostak", "Thomas Lindahl", "Paul Modrich", "Aziz Sancar",
             "James Allison", "Tasuku Honjo", "Harvey J. Alter", "Michael Houghton", "Charles M. Rice",
             "Ardem Patapoutian", "David Julius", "Syukuro Manabe", "Klaus Hasselmann", "Giorgio Parisi",
             "Benjamin List", "David W.C. MacMillan", "John B. Goodenough", "M. Stanley Whittingham", "Akira Yoshino",
             "Arthur Ashkin", "Gérard Mourou", "Donna Strickland", "Michel Mayor", "Didier Queloz", "James Peebles",
             "Eric Kandel", "Linda B. Buck", "Richard Axel", "Roderick MacKinnon", "Peter Agre", "Kurt Wüthrich",
             "Aaron Ciechanover", "Avram Hershko", "Irwin Rose", "Robert Huber", "Johann Deisenhofer", "Hartmut Michel",
             "Ernst Ruska", "Gerd Binnig", "Heinrich Rohrer", "Nicolaas Bloembergen", "Arthur L. Schawlow",
             "Charles H. Townes", "Dennis Gabor", "Gabriel Lippmann", "Henri Becquerel", "Pierre Curie",
             "Wilhelm Conrad Röntgen", "Albert A. Michelson", "Lord Rayleigh", "Philipp Lenard", "Johannes Stark",
             "Max von Laue", "William Henry Bragg", "William Lawrence Bragg", "Charles Glover Barkla",
             "Friedrich Schiller", "Jane Austen",
             "Fyodor Dostoevsky", "Leo Tolstoy", "James Joyce", "Virginia Woolf", "Marcel Proust",
             "Albert Camus", "Jean-Paul Sartre", "Simone de Beauvoir", "Aldous Huxley",
             "William Faulkner", "Gabriel García Márquez", "Jorge Luis Borges", "Umberto Eco",
             "Italo Calvino", "Milan Kundera", "Haruki Murakami", "Margaret Atwood", "Toni Morrison", "Chinua Achebe",
             "Wole Soyinka", "Chimamanda Ngozi Adichie", "Salman Rushdie",
             "Confucius", "Georg Wilhelm Friedrich Hegel",
             "Ludwig Wittgenstein", "Martin Heidegger", "Hannah Arendt", "Michel Foucault",
             "Jacques Derrida", "Judith Butler", "Slavoj Žižek", "Peter Singer", "Martha Nussbaum",
             "Alasdair MacIntyre", "John Rawls", "Robert Nozick", "Thomas Nagel", "Bernard Williams", "Derek Parfit",
             "Saul Kripke", "Hilary Putnam", "Donald Davidson", "Richard Rorty", "John Searle", "Noam Chomsky",
             "Daniel Dennett", "Patricia Churchland", "David Chalmers", "Thomas Kuhn", "Paul Feyerabend",
             "Imre Lakatos", "Karl Popper", "Gaston Bachelard", "Maurice Merleau-Ponty"]}


def show_rules():
    print("""
        --- Game Rules ---

        Welcome to "Who Am I?"! This is a single-player guessing game where you'll try to identify famous people based on AI-generated hints.

        Game Setup:
        - Select your difficulty level: Easy, Normal, or Hard.
        - Choose the number of rounds you want to play (2, 3, or 4).

        Gameplay:
        - At the start of each round, you'll receive 5 AI-generated hints related to a famous person.
        - Your goal is to guess who the person is.
        - Type your guess into the terminal.
        - You have multiple attempts to guess correctly.
        - The game will tell you if your guess is correct or incorrect.

        Scoring:
        - Easy Difficulty: 15 points for each correct guess, minus 1 point for each incorrect attempt.
        - Normal Difficulty: 30 points for each correct guess, minus 1 point for each incorrect attempt.
        - Hard Difficulty: 45 points for each correct guess, minus 1 point for each incorrect attempt.
        - If you use all attempts and guess incorrectly, you get 0 points for that round.
        - Your total score is the sum of points from all rounds.

        Hints:
        - You start with 5 hints at the beginning of each round.
        - Hints are provided to give you clues.

        Winning:
        - The game ends after the selected number of rounds.
        - Your final score will be displayed at the end.
        - Try to get the highest score possible!

        Additional Tips:
        - Take your time to think carefully before guessing.
        - Use hints wisely to maximize your score.
        - Have fun and learn about famous people!

        Type 'solution' to reveal the answer.
    """)
    input("press enter to return to main menu")


def get_article_title(difficulty):
    """Finds and returns a random title from title list, based on difficulty level. """
    return random.choice(difficulty_title_dict[difficulty.lower()])

def main():
    print("Rules description and difficulty themas list")

if __name__ == '__main__':
    main()