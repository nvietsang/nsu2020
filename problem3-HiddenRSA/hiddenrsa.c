//
// Created by nlag on 20/10/2020.
//
#include "gmp.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char * argv[]){
    mpz_t r2,r3,r6,r5,r10,r23,r25,n,e,res;
    mpz_inits(r2,r3,r6,r5,r10,r23,r25,n,e,res,NULL);
    mpz_set_str(r2,"50154912289039335014669339773308393642658123228965873078737860474494117389068",10);
    mpz_set_str(r3,"74177167678866806519929337366689313939300015489238864541679630476008627210599",10);
    mpz_set_str(r5,"66788051164865948223783605396869677445056352267867968640234839015540677264876",10);
    mpz_set_str(r6,"69732835711852253044075185248502970714729629373386336194927784886349053828079",10);
    mpz_set_str(r10,"36114573486270806055149334292830010504470514431479363437302273690048446896189",10);
//  find n
    mpz_mul(r23,r2,r3);
    mpz_sub(r23,r23,r6);
    mpz_mul(r25,r2,r5);
    mpz_sub(r25,r25,r10);
    mpz_gcd(n,r23,r25);
    gmp_printf("n = %Zu\n",n);

    int count = 0;
//  set e =  {3, 5, 17, 257 or 65537} and test a few cases
    mpz_set_ui(e,65537);
    mpz_set_ui(res,2);
    mpz_powm_ui(res,res,65537,n);
    if (mpz_cmp(res,r2)==0) count +=1;
    mpz_set_ui(res,3);
    mpz_powm_ui(res,res,65537,n);
    if (mpz_cmp(res,r3)==0) count +=1;
    mpz_set_ui(res,6);
    mpz_powm_ui(res,res,65537,n);
    if (mpz_cmp(res,r6)==0) count +=1;
    if (count == 3){
        gmp_printf("e = %Zu\n",e);
    } else {
        printf("wrong e value\n");
        return 0;
    }

    mpz_t p,q,d,phin,y,x;
    mpz_inits(p,q,d,phin,y,x,NULL);
    mpz_set_str(p,"232086664036792751646261018215123451301",10);
    mpz_set_str(q,"328328681700354546732404725320581286809",10);
//  check p and q then decrypt
    mpz_mul(res,p,q);
    if (mpz_cmp(res,n) != 0) {
        printf("wrong p and q value\n");
        return 0;
    }
    mpz_sub(phin,n,p);
    mpz_sub(phin,phin,q);
    mpz_add_ui(phin,phin,1);
    mpz_invert(d,e,phin);
    gmp_printf("d = %Zu\n",d);
    mpz_set_str(y,"71511896681324833458361392885184344933333159830863878600189212073777582178173",10);
    mpz_powm(x,y,d,n);
    gmp_printf("x = %Zu\n",x);

    mpz_clears(p,q,d,phin,y,x,NULL);
    mpz_clears(r2,r3,r6,r5,r10,r23,r25,n,e,res,NULL);
    return 0;
}