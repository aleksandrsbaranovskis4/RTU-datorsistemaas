public class score {
    public static void main(String[] args) {
        double[] atzimesParProgrammam = {1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1};
        double[] atzimesParKontroldarbiem = {9.09,6.67,9,0,4, 9,7,5,5.88,0, 8,3.5,8.33,10,8.43};
        double bonussPunktiParMenti = 0;
        double bonussPunktiParPapilduzdevumiem = 1;
        double bonussPunktiParAlgPraksi = 0;
        double atzimeParEksamenu = 0;

        atzimeParEksamenu = atzimeParEksamenu >= 4 ? atzimeParEksamenu : 0;

        double videjaAtzimeParLD = 0;
        for (int i=0; i<15; i++) {
            videjaAtzimeParLD = videjaAtzimeParLD + atzimesParProgrammam[i] * atzimesParKontroldarbiem[i];
        }

        videjaAtzimeParLD = videjaAtzimeParLD / 15;

        double bonussPunkti = (bonussPunktiParMenti + bonussPunktiParAlgPraksi + bonussPunktiParPapilduzdevumiem)* 0.1;
        long atzimeParKursu = Math.round(videjaAtzimeParLD * 0.6 + atzimeParEksamenu * 0.4 + bonussPunkti);
        atzimeParKursu = atzimeParKursu > 10 ? 10 : atzimeParKursu;
        System.out.println(atzimeParKursu);
    }
}
