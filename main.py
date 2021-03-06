import random
from Clases.Grafo import Grafo
from Clases.Arista import Arista
from Clases.Nodo import Nodo
from Clases.Modelos_grafos import grafoMalla, grafoErdosRenyi, grafoGilbert, grafoGeografico, grafoBarabasiAlbert, grafoDorogovtsevMendes


def main():
    path = ("C:\\Users\\Precision\\Desktop\\PROYECTO_1\\PROYECTO_3_MORENO_MENDIETA\\GV_FILES")

    Nodos_totales=[30,300]
    for nodos in Nodos_totales:
        m_erdos = random.randint(nodos+1,nodos*2)
        p_gilbert = random.uniform(0.1,1)
        r_geografico = random.uniform(0.1,1)
        d_barabasi = random.randint(1,nodos)
        malla_a=random.randint(2,nodos)
        malla_b=0
        if (nodos%malla_a==0):
            malla_b=nodos/malla_a
        else:
            while malla_b==0:
                malla_a-=1
                if (nodos%malla_a==0):
                    malla_b=nodos/malla_a
        malla_a=int(malla_a)
        malla_b=int(malla_b)

        grafito = grafoMalla(*(malla_a,malla_b))
        grafito.to_graphviz(path + grafito.id + ".gv")
        grafito.generar_pesos()
        dijkstra = grafito.Dijkstra(0)
        dijkstra.to_graphviz(path + dijkstra.id + ".gv")
      
       



        grafito = grafoErdosRenyi(nodos, m_erdos)
        grafito.to_graphviz(path + grafito.id + ".gv")
        grafito.generar_pesos()
        dijkstra = grafito.Dijkstra(0)
        dijkstra.to_graphviz(path + dijkstra.id + ".gv")
        print(f"g_nodes: {len(grafito.V)}")
        print(f"dijkstra_nodes: {len(dijkstra.V)}")

        grafito = grafoGilbert(nodos, p_gilbert, dirigido=False, auto=False)
        grafito.to_graphviz(path + grafito.id + ".gv")
        grafito.generar_pesos()
        dijkstra = grafito.Dijkstra(0)
        dijkstra.to_graphviz(path + dijkstra.id + ".gv")
        





        grafito = grafoGeografico(nodos, r_geografico)
        grafito.to_graphviz(path + grafito.id + ".gv")
        grafito.generar_pesos()
        dijkstra = grafito.Dijkstra(0)
        dijkstra.to_graphviz(path + dijkstra.id + ".gv")
        




        grafito = grafoBarabasiAlbert(nodos, d_barabasi, auto=False)
        grafito.to_graphviz(path + grafito.id + ".gv")
        grafito.generar_pesos()
        dijkstra = grafito.Dijkstra(0)
        dijkstra.to_graphviz(path + dijkstra.id + ".gv")
       



        grafito = grafoDorogovtsevMendes(nodos, dirigido=False)
        grafito.to_graphviz(path + grafito.id + ".gv")
        grafito.generar_pesos()
        dijkstra = grafito.Dijkstra(0)
        dijkstra.to_graphviz(path + dijkstra.id + ".gv")
       

if __name__ == "__main__":
        main()