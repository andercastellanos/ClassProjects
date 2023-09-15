public class FourOfAKind extends HandCategory {
    Rank highest;

    public FourOfAKind(Rank highest) {
        this.highest = highest;
    }

    @Override
    public String toString() {
        return "FourOfAKind [highest=" + highest + "]";
    }

    @Override
    int compareRank(Object right0) {
        FourOfAKind right = (FourOfAKind) right0;
        return highest.compareTo(right.highest);
    }

    @Override
    int category() {
        // TODO Auto-generated method stub
        return 3;
    }

}
