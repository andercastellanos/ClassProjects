public class FourOfAKind extends HandCategory { // Here, we're defining a new class named FourOfAKind. 
    // This class extends (inherits from) a class named HandCategory. This suggests that FourOfAKind is a type of HandCategory 
    
    Rank highest; //highest of type Rank.
    //This variable probably represents the rank (like Ace, King, Queen, etc.) of the highest card in the Four of a Kind.

    public FourOfAKind(Rank highest) { //Here, we're defining the constructor of the FourOfAKind class. 
        //This constructor accepts a single argument: the highest rank card in the Four of a Kind.
        
        this.highest = highest; //In the constructor, we're assigning the passed highest value to the class's instance variable named highest. 
        //This allows us to store and later use the rank of the highest card in the Four of a Kind.
    } 

    @Override //. By using @Override, you're indicating that you're providing a new version of the toString() method specifically for the FourOfAKind class.
    public String toString() { //This declares a method named toString which will return a String when it's called.

        return "FourOfAKind [highest=" + highest + "]"; //This line constructs a String and returns it.
    }

    @Override // over riding a method from a super class 
    int compareRank(Object right0)
    // This declares a method named compareRank which will accept one arguement of type Object named right0
    { 

       FourOfAKind right = (FourOfAKind) right0; 
        //After this line, the right variable now refers to the right0 object, but as a FourOfAKind object.

        
         return highest.compareTo(right.highest);
        //This method provides a way to compare two FourOfAKind objects based on their rank. 
        //It could be used for sorting purposes or determining which hand is stronger in a game.
        
    }

    @Override // The method Category is overriding the super class 
    int category() {
       
        return 3; // returning 3 because there is 3 categories in the Four of a kind Class 
        //this method seems to be to provide a consistent way to identify or categorize an instance of FourOfAKind
    }

}
