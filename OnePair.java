public class OnePair extends HandCategory {
    Rank highest;

    public OnePair(Rank highest) {
        this.highest = highest;
    }

    @Override
    public String toString() {
        return "OnePair [highest=" + highest + "]";
    }

    @Override
    int compareRank(Object right0) {

        OnePair right = (OnePair) right0;
        return highest.compareTo(right.highest);
    }

    @Override
    int category() {
        // TODO Auto-generated method stub
        return 9;
    }

}
