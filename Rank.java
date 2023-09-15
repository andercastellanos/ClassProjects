public enum Rank {
    r2, r3, r4, r5, r6, r7, r8, r9, r10, jack, queen, king, ace;

    public String toString() {
        switch (this) {
            case ace:
                return "Ace";
            case r2:
                return "2";
            case r3:
                return "3";
            case r4:
                return "4";
            case r5:
                return "5";
            case r6:
                return "6";
            case r7:
                return "7";
            case r8:
                return "8";
            case r9:
                return "9";
            case r10:
                return "10";
            case jack:
                return "Jack";
            case queen:
                return "Queen";
            case king:
                return "King";
        }
        throw new RuntimeException("Unknown Case");
    }

    public String fileSection() {
        switch (this) {
            case ace:
                return "ace";
            case r2:
                return "2";
            case r3:
                return "3";
            case r4:
                return "4";
            case r5:
                return "5";
            case r6:
                return "6";
            case r7:
                return "7";
            case r8:
                return "8";
            case r9:
                return "9";
            case r10:
                return "10";
            case jack:
                return "jack";
            case queen:
                return "queen";
            case king:
                return "king";
        }
        throw new RuntimeException("Unknown Case");
    }

    public Rank next(int n) {
        for (int i = 0; i < values().length; i++) {
            if (values()[i] == this) {
                return values()[i + n];
            }
        }
        throw new RuntimeException("Unknown Case");
    }

    // inclusive
    public static Rank[] range(Rank lower, Rank higher) {
        int count = 0;
        Rank current = lower;
        while (current != higher) {
            count++;
            current = current.next(1);
        }
        Rank[] result = new Rank[count + 1];
        for (int i = 0; i < count; i++) {
            result[i] = lower;
            lower = lower.next(1);
        }
        result[count] = higher;
        return result;
    }

}
