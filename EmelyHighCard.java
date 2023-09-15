import java.util.Arrays;

public class HighCard extends HandCategory {
    Rank[] ranks;

    public HighCard(Rank[] ranks) {
        this.ranks = ranks;
    }

    @Override
    public String toString() {
        return "HighCard [ranks=" + Arrays.toString(ranks) + "]";
    }

    @Override
    int compareRank(Object right0) {

        HighCard right = (HighCard) right0;
        for (int i = 4; i > 0; i--) {
            int high = ranks[i].compareTo(right.ranks[i]);
            if (high != 0) {
                return high;
            }
        }
        return ranks[0].compareTo(ranks[0]);
    }

    @Override
    int category() {
        // TODO Auto-generated method stub
        return 10;
    }

}
