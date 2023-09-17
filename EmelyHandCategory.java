public abstract class HandCategory implements Comparable<HandCategory> {
    // Abstract method for comparing the rank of two hands
    abstract int compareRank(Object right);

    // Abstract method for determining the category of the hand
    abstract int category();

    // Implementation of the compareTo method for comparing HandCategory objects
    public int compareTo(HandCategory right) {
        // Compare the categories of two hand categories
        if (category() < right.category()) {
            return 1; // Return 1 if this hand's category is higher
        } else if (category() > right.category()) {
            return -1; // Return -1 if this hand's category is lower
        } else {
            // If the categories are the same, delegate the comparison to compareRank
            return this.compareRank(right);
        }
    }
}
