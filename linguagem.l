%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "linguagem.tab.h"
%}

DIGITO [0-9]

%%

"var"                                   { printf("Token VAR\n"); return VAR; }
"funcao"                                { printf("Token FUNCAO\n"); return FUNCAO; }
"se"                                    { printf("Token SE\n"); return SE; }
"senao"                                 { printf("Token SENAO\n"); return SENAO; }
"para"                                  { printf("Token PARA\n"); return PARA; }
"inteiro"                               { printf("Token INTEIRO\n"); return INTEIRO; }
"flutuante"                             { printf("Token FLUTUANTE\n"); return FLUTUANTE; }
"texto"                                 { printf("Token TEXTO\n"); return TEXTO; }
"booleano"                              { printf("Token BOOLEANO\n"); return BOOLEANO; }
"verdadeiro"                            { printf("Token VERDADEIRO\n"); return VERDADEIRO; }
"falso"                                 { printf("Token FALSO\n"); return FALSO; }
"+"                                     { printf("Token SOMA\n"); return SOMA; }
"-"                                     { printf("Token SUBTRACAO\n"); return SUBTRACAO; }
"*"                                     { printf("Token MULTIPLICACAO\n"); return MULTIPLICACAO; }
"/"                                     { printf("Token DIVISAO\n"); return DIVISAO; }
">"                                     { printf("Token MAIOR_QUE\n"); return MAIOR_QUE;}
"<"                                     { printf("Token MENOR_QUE\n"); return MENOR_QUE;}
[a-zA-Z][a-zA-Z0-9]*                    { printf("Token IDENTIFICADOR\n"); return IDENTIFICADOR; }
{DIGITO}+"."{DIGITO}+                   { printf("Token LITERAL_FLUTUANTE\n"); return LITERAL_FLUTUANTE; }
{DIGITO}+                               { printf("Token LITERAL_NUMERICO\n"); return LITERAL_NUMERICO; }
\"([^\\\"]|\\.)*\"                      { printf("Token LITERAL_TEXTO\n"); return LITERAL_TEXTO; }
";"                                     { printf("Token PONTO_E_VIRGULA\n"); return PONTO_E_VIRGULA; }
"="                                     { printf("Token IGUAL\n"); return IGUAL; }
","                                     { printf("Token VIRGULA\n"); return VIRGULA; }
"("                                     { printf("Token ABRE_PARENTESES\n"); return ABRE_PARENTESES; }
")"                                     { printf("Token FECHA_PARENTESES\n"); return FECHA_PARENTESES; }
"{"                                     { printf("Token ABRE_CHAVES\n"); return ABRE_CHAVES; }
"}"                                     { printf("Token FECHA_CHAVES\n"); return FECHA_CHAVES; }
[ \t\n]                                 { /* Ignora espaços em branco */ }
.                                       { fprintf(stderr, "Caractere não reconhecido: %c\n", yytext[0]); }

%%

