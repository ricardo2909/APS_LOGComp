/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_LINGUAGEM_TAB_H_INCLUDED
# define YY_YY_LINGUAGEM_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    VAR = 258,                     /* VAR  */
    FUNCAO = 259,                  /* FUNCAO  */
    SE = 260,                      /* SE  */
    SENAO = 261,                   /* SENAO  */
    PARA = 262,                    /* PARA  */
    INTEIRO = 263,                 /* INTEIRO  */
    FLUTUANTE = 264,               /* FLUTUANTE  */
    TEXTO = 265,                   /* TEXTO  */
    BOOLEANO = 266,                /* BOOLEANO  */
    VERDADEIRO = 267,              /* VERDADEIRO  */
    FALSO = 268,                   /* FALSO  */
    IDENTIFICADOR = 269,           /* IDENTIFICADOR  */
    LITERAL_NUMERICO = 270,        /* LITERAL_NUMERICO  */
    LITERAL_TEXTO = 271,           /* LITERAL_TEXTO  */
    LITERAL_FLUTUANTE = 272,       /* LITERAL_FLUTUANTE  */
    SOMA = 273,                    /* SOMA  */
    SUBTRACAO = 274,               /* SUBTRACAO  */
    MULTIPLICACAO = 275,           /* MULTIPLICACAO  */
    DIVISAO = 276,                 /* DIVISAO  */
    IGUAL = 277,                   /* IGUAL  */
    VIRGULA = 278,                 /* VIRGULA  */
    ABRE_PARENTESES = 279,         /* ABRE_PARENTESES  */
    FECHA_PARENTESES = 280,        /* FECHA_PARENTESES  */
    ABRE_CHAVES = 281,             /* ABRE_CHAVES  */
    FECHA_CHAVES = 282,            /* FECHA_CHAVES  */
    PONTO_E_VIRGULA = 283,         /* PONTO_E_VIRGULA  */
    MAIOR_QUE = 284,               /* MAIOR_QUE  */
    MENOR_QUE = 285                /* MENOR_QUE  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_LINGUAGEM_TAB_H_INCLUDED  */
