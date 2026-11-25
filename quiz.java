import java.util.Scanner;

public class quiz {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String[][] fragor = {{"Fråga 1\n342 är jämnt delbart med 3.", "1"},
                            {"Fråga 2\nChokladmjölk kommer från bruna kor.", "2"},
                            {"Fråga 3\nMalmö ligger i Skåne","1"},
                            {"Fråga 4\nAstrid Lindgren skrev \"Pippi Långstrump\"", "1"},
                            {"Fråga 5\nKAJ vann eurovision 2025", "2"},
                            {"Fråga 6\n\"AI\" står för \"Artificial Intelligence\"","1"},
                        }; //Fält med alla frågor och alternativ och svar
        int svar; //Variabel som kommer tillfälligt spara varje svar

        //Vid start är alla antal 0
        int poang = 0;
        //Skriv ut information
        System.out.println("Klarar du mitt quiz?");
        System.out.println("Svara på frågorna genom att ange \"1\"eller \"2\"");

        //For-sats, varje loop hanterar en av frågorna i fältet "fragor"
        for (int i = 0; i < fragor.length; i++) {
            System.out.println("--------------------------------------");//Gör det lites snyggt
            
            //Ställ fråga och hämta svar
            System.out.print(fragor[i][0]);

            boolean svarSaknas = true;
            while(svarSaknas){
                System.out.print("\n1.Sant\n2.Falskt\nSvar: ");
                svar = input.nextInt();

                svarSaknas = false;
                //Om korrekt svar så ökas poäng
                if((svar == Integer.parseInt(fragor[i][1]))){
                    poang++;
                //Om ogiltigt svar så får man försöka igen
                }else if(!((svar == 1) || (svar == 2))){
                    System.out.println("Felinmatning, prova igen");
                    svarSaknas = true;
                }
            }
        }

        System.out.println("--------------------------------------");
        System.out.println("Poäng: " + poang + " av 6");
    }
}
