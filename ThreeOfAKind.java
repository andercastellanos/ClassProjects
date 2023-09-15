public class ThreeOfAKind extends HandCategory {
    Rank highest;

    public ThreeOfAKind(Rank highest) {
        this.highest = highest;
    }

    @Override
    public String toString() {
        return "ThreeOfAKind [highest=" + highest + "]";
    }

    @Override
    int compareRank(Object right0) {
        ThreeOfAKind right = (ThreeOfAKind) right0;
        return highest.compareTo(right.highest);
    }

    @Override
    int category() {
        return 7;
    }

}
