import java.util.Arrays;

public class Player { // Declare a class named "Player"
    Card[] hand; // Declare a Java array named "hand" of type Card.
    int holdings; // Declare an integer value named "holdings".

    Player() {
        hand = new Card[5];
        holdings = 500;
    }

    // return null when it differs
    public static Suit sameSuit(Card[] hand) {
        Suit initial = hand[0].suit;
        for (int i = 0; i < 5; i++) {
            if (initial != hand[i].suit) {
                return null;
            }
        }
        return initial;
    }

    public static int countRank(Card[] hand, Rank rank) {
        int count = 0;
        for (Card card : hand) {
            if (card.rank == rank) {
                count++;
            }
        }
        return count;
    }

    public static Rank highestRank(Card[] hand) {
        Rank[] ranks = new Rank[hand.length];
        for (int i = 0; i < hand.length; i++) {
            ranks[i] = hand[i].rank;
        }
        Arrays.sort(ranks);
        return ranks[ranks.length - 1];
    }

    // returns null when it doesn't match
    public RoyalFlush royalFlush() {
        Suit suit = sameSuit(hand);
        if (suit == null) {
            return null;
        }
        Rank current = Rank.ace;
        for (Card card : hand) {
            if (card.rank != current) {
                return null;
            }
            current = current.next(-1);
        }
        return new RoyalFlush(suit);
    }

    // returns null when it doesn't match
    public StraightFlush straightFlush() {
        Suit suit = sameSuit(hand);
        if (suit == null) {
            return null;
        }
        straight: for (Rank rank : Rank.range(Rank.r5, Rank.king)) {
            Rank current = rank;
            for (Card card : hand) {
                if (card.rank != current) {
                    continue straight;
                }
                current = current.next(-1);
            }
            return new StraightFlush(rank, suit);
        }

        return null;
    }

    public FullHouse fullHouse() {
        for (Rank rank : Rank.range(Rank.r2, Rank.king)) {
            if (countRank(hand, rank) == 3) {
                for (Rank rank2 : Rank.range(rank.next(1), Rank.ace)) {
                    if (countRank(hand, rank2) == 2) {
                        return new FullHouse(rank);
                    }
                }
            }
        }

        return null;
    }

    public Flush flush() {
        Suit suit = sameSuit(hand);
        if (suit != null) {
            return new Flush(highestRank(hand));
        }
        return null;
    }

    public Straight straight() {
        straight: for (Rank rank : Rank.range(Rank.r5, Rank.ace)) {
            Rank current = rank;
            for (Card card : hand) {
                if (card.rank != current) {
                    continue straight;
                }
                current = current.next(-1);
            }
            return new Straight(rank);
        }
        return null;
    }

    // returns null when it doesn't match
    public FourOfAKind fourOfAKind() {
        for (Rank rank : Rank.values()) {
            if (countRank(hand, rank) == 4) {
                return new FourOfAKind(rank);
            }
        }
        return null;
    }

    // returns null when it doesn't match
    public ThreeOfAKind threeOfAKind() {
        for (Rank rank : Rank.values()) {
            if (countRank(hand, rank) == 3) {
                return new ThreeOfAKind(rank);
            }
        }
        return null;
    }

    public TwoPair twoPair() {
        for (Rank rank : Rank.range(Rank.r2, Rank.king)) {
            if (countRank(hand, rank) == 2) {
                for (Rank rank2 : Rank.range(rank.next(1), Rank.ace)) {
                    if (countRank(hand, rank2) == 2) {
                        return new TwoPair(rank2, rank);
                    }
                }
            }
        }

        return null;
    }

    public OnePair onePair() {
        for (Rank rank : Rank.range(Rank.r2, Rank.king)) {
            if (countRank(hand, rank) == 2) {
                return new OnePair(rank);
            }
        }

        return null;
    }

    public HighCard highCard() {
        Rank[] ranks = new Rank[hand.length];
        for (int i = 0; i < hand.length; i++) {
            ranks[i] = hand[i].rank;
        }
        Arrays.sort(ranks);
        return new HighCard(ranks);
    }

    public HandCategory categorize() {
        HandCategory category = null;
        category = royalFlush();
        if (category != null) {
            return category;
        }

        category = straightFlush();
        if (category != null) {
            return category;
        }

        category = fourOfAKind();
        if (category != null) {
            return category;
        }
        category = fullHouse();
        if (category != null) {
            return category;
        }
        category = flush();
        if (category != null) {
            return category;
        }
        category = straight();
        if (category != null) {
            return category;
        }

        category = threeOfAKind();
        if (category != null) {
            return category;
        }

        category = twoPair();
        if (category != null) {
            return category;
        }

        category = onePair();
        if (category != null) {
            return category;
        }

        category = highCard();
        if (category != null) {
            return category;
        }
        return null;
    }

}
