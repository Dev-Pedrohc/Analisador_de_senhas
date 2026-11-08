# Analisador de Senhas

Programa em Python, executado no terminal, que analisa a força de uma senha digitada pelo usuário e a classifica como fraca, média ou forte.

## Como funciona
O programa percorre a senha caractere por caractere e conta quantas letras maiúsculas, minúsculas, números e símbolos ela tem. Depois soma pontos de acordo com as regras abaixo.

## Regras de pontuação
| Critério | Pontos |
|---|---|
| 2 ou mais maiúsculas | 2 |
| 1 maiúscula | 1 |
| 2 ou mais minúsculas | 2 |
| 1 minúscula | 1 |
| 2 ou mais números | 2 |
| 1 número | 1 |
| 1 ou mais símbolos | 1 |
| Tamanho de 8 ou mais caracteres (CONFIRME NO SEU CÓDIGO) | 1 |

**Classificação:** 0 a 3 pontos = Fraca · 4 a 7 = Média · 8 = Forte

## Como rodar
1. Tenha o Python 3 instalado.
2. Baixe ou clone este repositório.
3. No terminal, dentro da pasta do projeto, execute:

python main.py

## Exemplo
(Cole aqui um print do terminal ou o texto de uma execução real)

## Próximos passos
- [ ] Mostrar a pontuação e o que falta para melhorar a senha
- [ ] Cores no terminal
- [ ] Menu e gerador de senhas

## Autor
Pedro — estudante de Ciências da Computação