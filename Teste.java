public class Teste{
  public static void main(String[] args){
    if(!condicao("1") || condicao("2") ){
      System.out.println("ola mundo");      
    }
  }

  public static boolean condicao(String str){
    System.out.println(str);
    return true;
  }
  
}