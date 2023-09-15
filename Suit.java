public enum Suit {
    clubs, diamonds, hearts, spades;

    public String toString() {
        switch (this) {
            case clubs:
                return "Clubs";
            case diamonds:
                return "Diamonds";
            case hearts:
                return "Hearts";
            case spades:
                return "Spades";
        }
        throw new RuntimeException("Unknown Case");
    }

    public String fileSection() {
        switch (this) {
            case clubs:
                return "clubs";
            case diamonds:
                return "diamonds";
            case hearts:
                return "hearts";
            case spades:
                return "spades";
        }
        throw new RuntimeException("Unknown Case");
    }

    public Suit next(int n) {
        for (int i = 0; i < values().length; i++) {
            if (values()[i] == this) {
                return values()[i + n];
            }
        }
        throw new RuntimeException("Unknown Case");
    }
}
