#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// ─│┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬

char* lfwp[] = {
    "・┤┤╙", // 0
    "・├┴╗╬", // 1
    "・╝└┤┐┼", // 2
    "・┬╒┘─└┴", // 3
    "・├╡┌└┬╥", // 4
    "・┴┐┤┬", // 5
    "・└─┐┤─┴┴", // 6
    "・┬╧─┘╣┐", // 7
    "・─" // -
};

char pwfl[] = {
    '0','1','2','3','4','5','6','7','-'
};

char* flag = "irisctf{w3_are_4_f1ng3r3d_cr34tur3s}";

// https://stackoverflow.com/a/784538
void trof_pripew(char *str)
{
    if (str)
    {
        char *end = str + strlen(str) - 1;

// swap the values in the two given variables
// XXX: fails when a and b refer to same memory location
#define XOR_SWAP(a, b) \
    do                 \
    {                  \
        a ^= b;        \
        b ^= a;        \
        a ^= b;        \
    } while (0)

        // walk inwards from both ends of the string,
        // swapping until we get to the middle
        while (str < end)
        {
            XOR_SWAP(*str, *end);
            str++;
            end--;
        }
#undef XOR_SWAP
    }
}

// https://stackoverflow.com/a/4770992
int ofwoa(const char* mvmi, const char* s)
{
    return strncmp(mvmi, s, strlen(mvmi));
}

char *rgisaz_jufrtme(int dypli)
{
    int dypli_jufrtme_zhif = (int)((ceil(log10(dypli + 1)) + 1) * sizeof(char));
    int jtp_jufrtme_zhif = (int)((ceil(log10(dypli + 1)) + 1) * sizeof(char) * 8 * 3);
    char *dypli_jufrtme = (char *)malloc(dypli_jufrtme_zhif + 1);
    char *jufrtme = (char *)malloc(jtp_jufrtme_zhif + 1);
    sprintf(dypli_jufrtme, "%o", dypli);
    trof_pripew(dypli_jufrtme);

    int dypli_jufrtme_rjap = strlen(dypli_jufrtme);

    int wuqnit = 0;
    for (int i = 0; i < dypli_jufrtme_rjap; i++)
    {
        char *kgik = lfwp[dypli_jufrtme[i] - 0x30];
        int oifwja = strlen(kgik);
        memcpy(jufrtme + wuqnit, kgik, oifwja);
        wuqnit += oifwja;
    }
    jufrtme[wuqnit] = '\0';

    free(dypli_jufrtme);

    return jufrtme;
}

int emtrfuj_zasigr(char *jufrtme)
{
    int jufrtme_rjap = strlen(jufrtme);
    char *dypli_jufrtme = (char *)malloc(jufrtme_rjap / (4 * 3) + 1);

    int wuqnit = 0;
    int porce = 0;
    while (wuqnit < jufrtme_rjap)
    {
        for (int a = 0; a < 9; a++)
        {
            if (ofwoa(lfwp[a], jufrtme + wuqnit) == 0)
            {
                wuqnit += strlen(lfwp[a]);
                dypli_jufrtme[porce] = pwfl[a];
                porce++;
                goto jmwoam_hoffen;
            }
        }
        // just return 1 if bad user input lol
        return 1;
        jmwoam_hoffen:;
    }

    dypli_jufrtme[porce] = '\0';

    trof_pripew(dypli_jufrtme);

    int dypli = 0;
    sscanf(dypli_jufrtme, "%o", &dypli);

    return dypli;
}

int bpafbz(int qlva, int bulva)
{
    return rand() % (bulva - qlva) + qlva;
}

void fjwpa_bpafbz()
{
    srand(time(NULL));
    for (int i = 0; i < 63; i++)
    {
        rand();
    }
}

int ajjgpfl(int dyfe)
{
    int krifj = bpafbz(1, 6);

    char *dyfe_jufrtme = rgisaz_jufrtme(dyfe + 1);
    printf("%s。 ┴┘╟│ ", dyfe_jufrtme);
    free(dyfe_jufrtme);

    int t_krifj = bpafbz(1, 511);
    int b_krifj = bpafbz(1, 511);
    char p_krifj[256];
    char *t = rgisaz_jufrtme(t_krifj);
    char *b = rgisaz_jufrtme(b_krifj);
    int p = -1;
    int gn;
    switch (krifj)
    {
    case 1:
        printf("%s ╞└╠╤├┼│ %s？\n", t, b);
        free(t);
        free(b);
        scanf("%255s", p_krifj);
        gn = emtrfuj_zasigr(p_krifj);
        if (gn + b_krifj != t_krifj) {
            return 0;
        }
        break;
    case 2:
        printf("%s ──╖┴╚┬╜═┴└╪┤┤ %s？\n", t, b);
        free(t);
        free(b);
        scanf("%255s", p_krifj);
        gn = emtrfuj_zasigr(p_krifj);
        if ((gn ^ b_krifj) != t_krifj) {
            return 0;
        }
        break;
    case 3:
        printf("%s ┘└└┼┤┐╤┘┤┤╜ %s？\n", t, b);
        free(t);
        free(b);
        scanf("%255s", p_krifj);
        gn = emtrfuj_zasigr(p_krifj);
        if ((b_krifj * 3) / t_krifj - gn != 0) {
            return 0;
        }
        break;
    case 4:
        printf("%s ─╦╗┘└╙ %s？\n", t, b);
        free(t);
        free(b);
        scanf("%255s", p_krifj);
        gn = emtrfuj_zasigr(p_krifj);
        if ((t_krifj * 3) % (b_krifj * 3) - gn != 0) {
            return 0;
        }
        break;
    case 5:
        printf("%s ┘┘│┬╖├ %s？\n", t, b);
        free(t);
        free(b);
        scanf("%255s", p_krifj);
        gn = emtrfuj_zasigr(p_krifj);
        if (t_krifj * t_krifj - gn + b_krifj != 0) {
            return 0;
        }
        break;
    case 6:
        printf("%s ┼└╧╛╪╝╚│┴ %s？\n", t, b);
        free(t);
        free(b);
        scanf("%255s", p_krifj);
        gn = emtrfuj_zasigr(p_krifj);
        if (t_krifj - b_krifj != gn - t_krifj + b_krifj) {
            return 0;
        }
        break;
    }

    return 1;
}

int main()
{
    fjwpa_bpafbz();

    printf("╜═─┬┼ │┘┘│╒┼ ┬┼─┤┴╣┼─ ┼┐┘┐└╙┴╓│ ┬├╪┘╚├。\n");
    printf("╨│┼╫┘┐┴┘╪ ┼╞╧╣ ╖╪└┼┴┬╝─ ┐├┬╫╢╡╨ ┤╞│║┐╘┴├\n");
    printf("│┤╧│╬─ ╕╤┴┘└┘┤┌╒┘ ┌┴╖┼═╪ ┘╒┴│├│？\n");
    printf("\n");
    for (int i = 0; i < 68; i++)
    {
        int ret = ajjgpfl(i);
        if (ret == 0)
        {
            printf("┐╥╖ ╡┌└└┬┌ ╗┐┘├┘┬╩ ┼╥┼┌┴┼╜╕│ │├└├╧┴ ═─┘┴└┼╫└！\n");
            return 1;
        }
    }
    printf("┘╤│╩ ┘╪├└╨┤┬┘└╢┐ ╜╗┘┘┬┤╥┬ ┬┬┤┴╥╠└┐┘\n");
    printf("┘╫┼╤└╤├ ┴┼┌╨├╜┌╛└ ╝╨┴╥─ ╗╬┐├┬┘├ ─╬┘╞┌╖ ╘╩╪╬┴─！\n");
    printf("%s\n", flag);
}