                                            ---- Práticas Agrupamentos de Dados ----

1.	Inicialmente devemos abrir o terminal e dirigir até a pasta praticas/

2.	Para que seja possível rodar o programa é necessário criarmos um ambiente virtual, passa isso rodamos o seguinte comando no terminal:
		> python3 -m venv venv

3.	Para usarmos o ambiente criado executamos:
		> source venv/bin/activate

4.	Com o ambiente já configurado, precisamos agora instalar todas as dependências necessárias para rodar o programa
		> pip install -r requirements.txt

                                                    ---- Prática 2 ----

5.	Para executarmos então rodamos:
		> python3 main.py {arg1} {arg2}

	- O arg1 refere-se ao nome do arquivo .csv da base de dados que deve estar dentro do diretório praticas/src/files IMPORTANTE: A extensão deve ser passada
	- O arg2 refere-se a quantidade de atributos que cada objeto possui, para que seja feita uma validação de todos os dados antes que sejam estimados

6. Ao final, será gerado um novo arquivo .cvs dentro de praticas/src/files/results com o resultado do algoritmo


                                                    ---- Prática 4 ----

5.	Para executarmos então rodamos:
		> python3 main.py {arg1} {arg2} {arg3}

	- O arg1 refere-se ao nome do arquivo .csv da base de dados que deve estar dentro do diretório praticas/src/files IMPORTANTE: A extensão deve ser passada
	- O arg2 refere-se a quantidade de atributos que cada objeto possui, para que seja feita uma validação de todos os dados antes que sejam estimados
	- Tipo do cálculo de distância, esse pode ser dos tipos:
	    1. euclidean (Distância Euclidiana)
	    2. manhattan (Distância Manhattan)

6. Ao final, será gerado um novo arquivo .txt dentro de praticas/src/files/results com o resultado do algoritmo

													---- Prática 6 ----

5.	Para executarmos então rodamos:
		> python3 pratice_6.py {arg1} {arg2}

	- O arg1 refere-se ao nome do arquivo .csv da base de dados que deve estar dentro do diretório praticas/src/files IMPORTANTE: A extensão deve ser passada
	- O arg2 refere-se a quantidade de centroídes K

6. Ao final, será gerado um novo arquivo .txt dentro de praticas/src/files/results com o resultado do algoritmo, que montará os grupos juntamento com seus centroídes