import java.util.Random;
import java.util.Scanner;

public class Game {
    Card[] deck;
    int index;
    Random rng;
    int pot;
    int condition = 0;
    // 0 is initial, 1 middle, 2 final bet
    Player player;
    Player dealer;
    Scanner scanner;

    Game(int seed, Scanner scanner) {
        deck = new Card[52];
        Rank[] ranks = Rank.values();
        Suit[] suits = Suit.values();
        int i = 0;
        for (Rank rank : ranks) {
            for (Suit suit : suits) {
                deck[i] = new Card(suit, rank);
                i++;
            }
        }

        rng = new Random(seed);
        player = new Player();
        dealer = new Player();
        this.scanner = scanner;
    }

    void bet(String name, Player player, int bet) throws LoseException {
        if (bet > player.holdings) {
            throw new LoseException(name, player);
        }
        System.out.println(name + " bets " + bet);
        player.holdings -= bet;
        pot += bet;
    }

    void reward(String name, Player player) {
        System.out.println(name + " wins " + pot);
        player.holdings += pot;
        pot = 0;
    }

    void shuffle() {
        for (int i = 0; i < deck.length; i++) {
            // Generate an index randomly
            int index = rng.nextInt(deck.length - i) + i;
            Card temp = deck[i];
            deck[i] = deck[index];
            deck[index] = temp;
        }
        index = 0;
    }

    void deal(Player player) {
        for (int i = 0; i < 5; i++) {
            player.hand[i] = deck[index];
            index++;
        }
    }

    void showHand(String name, Player player) {
        System.out.println(name);
        for (int i = 0; i < 5; i++) {
            System.out.println(i + ": " + player.hand[i]);
        }
    }

    void swap(String name, Player player) {
        showHand(name, player);
        System.out.println("How many cards would you like to swap?");
        // todo chech less 3
        int num = scanner.nextInt();
        for (int i = 0; i < num; i++) {
            System.out.println("Choose your index");
            showHand(name, player);
            int handIndex = scanner.nextInt();
            player.hand[handIndex] = deck[index];
            index++;
        }
    }

    void showState() {
        System.out.println("Player:" + player.holdings);
        System.out.println("Dealer:" + dealer.holdings);
    }

    int chooseInitial() {
        System.out.println("Bet(0) or Fold(1)?");
        return scanner.nextInt();
    }

    int choosePlayerFinal() {
        System.out.println("Bet(0), Fold(1), Call(2), or All in(3)?");
        return scanner.nextInt();
    }

    int chooseDealerFinalBet() {
        System.out.println("Fold(1), Call(2), or All in(3)?");
        return scanner.nextInt();
    }

    int chooseDealerFinalCall() {
        System.out.println("Fold(1), or All in(3)?");
        return scanner.nextInt();
    }

    void pickWinner() {
        HandCategory playerCat = player.categorize();
        HandCategory dealerCat = dealer.categorize();
        System.out.println("Player");
        System.out.println(playerCat);
        System.out.println("Dealer");
        System.out.println(dealerCat);
        if (playerCat.compareTo(dealerCat) > 0) {
            System.out.println("Player wins");
            reward("Player", player);
        } else {
            System.out.println("Dealer wins");
            reward("Dealer", dealer);
        }
    }

    void allIn(String playerName, Player player, String dealerName, Player dealer) throws LoseException {
        bet(playerName, player, player.holdings);
        System.out.println(dealerName);
        int option = chooseDealerFinalCall();
        if (option == 1) {
            reward(playerName, player);
        } else if (option == 3) {
            bet(dealerName, dealer, dealer.holdings);
            pickWinner();
        }
    }

    void gameLoop() {
        int option = 0;
        try {
            while (true) {
                showState();
                bet("Player", player, 5);
                bet("Dealer", dealer, 5);
                shuffle();
                deal(player);
                deal(dealer);

                showHand("Player", player);

                option = chooseInitial();

                if (option == 1) {
                    reward("Dealer", dealer);
                    continue;
                }

                showHand("Dealer", dealer);
                option = chooseInitial();

                if (option == 1) {
                    reward("Player", player);
                    continue;
                }

                bet("Player", player, 5);
                bet("Dealer", dealer, 5);
                showState();

                swap("Player", player);
                swap("Dealer", dealer);

                System.out.println("What do you wish to do Player?");
                option = choosePlayerFinal();

                if (option == 0) {
                    bet("Player", player, 5);
                    // bet
                    // dealer: fold, call or all in
                    System.out.println("What do you wish to do Dealer?");
                    option = chooseDealerFinalBet();
                    if (option == 1) {
                        reward("Player", player);
                    } else if (option == 2) {
                        // player bet, dealer called
                        pickWinner();
                    } else if (option == 3) {
                        allIn("Dealer", dealer, "Player", player);
                    }
                } else if (option == 1) {
                    // player folds
                    reward("Dealer", dealer);
                } else if (option == 2) {
                    // player calls
                    // dealer: fold or all in
                    System.out.println("Dealer");
                    option = chooseDealerFinalCall();
                    if (option == 1) {
                        reward("Player", player);
                    } else if (option == 3) {
                        allIn("Dealer", dealer, "Player", player);
                    }
                } else if (option == 3) {
                    allIn("Player", player, "Dealer", dealer);
                }
            }
        } catch (LoseException loser) {
            System.out.println(loser.name + " Lost");
        }
    }

    public static void main(String[] args) {
        //int seed = Integer.parseInt(args[0]);
        int seed = 0;
        Scanner scanner = new Scanner(System.in);

        while (true) {
            new Game(seed, scanner).gameLoop();
            System.out.println("Do you want to play a new game? Yes(0) No(1)");
            int option = scanner.nextInt();
            if (option == 1) {
                break;
            }
        }
    }
}
