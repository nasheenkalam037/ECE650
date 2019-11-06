#include <iostream>
#include<string>
#include<queue>
#include<vector>
#include<bits/stdc++.h>

#define arraySIZE 100

using namespace std;

int i,j;
int startpoint;
int endpoint;
int aArray[arraySIZE][arraySIZE];
int number_of_vertice;
queue <int> queue_of_points;
int visited[arraySIZE],distance_value[arraySIZE];
int previous[arraySIZE];
char e2,c;

void check_input();
void vertices();
void add_edge();
void startandendpoint();
void shortest_path();

void matrixInitialize();
void PrintMatrix();
void bfs(int aArray[][arraySIZE],int number_of_vertice,int startpoint,int endpoint);
//void initiate_bfs(int startpoint);
void printShortest(int startpoint,int endpoint);
void clearqueue( queue<int> &queue_of_points );




void vertices()
{
    matrixInitialize();
    cin>>number_of_vertice;

}


void add_edge()
{
    //matrixInitialize();
    //char e2;
    //int i,j;
    cin>>e2;
    while (e2 !='}')
        {
            cin>>e2>>i>>e2>>j>>e2>>e2;
            if (i<number_of_vertice && j<number_of_vertice)
            {
                aArray[i][j]=aArray[j][i]=1;
            }
            else
            {
                cout<<"Error: Vertex does not exist. "<<endl;
                continue;
            }

        }

}

void startandendpoint()
{
    cin>>startpoint>>endpoint;

}

void matrixInitialize()
    {
        for(i=0;i<100;i++)
            {
                for(j=0;j<100;j++)
                {
                    aArray[i][j] = 0;
                }
            }
    }

//    void initiate_bfs(int startpoint)
//{
//    for(int i=0;i<number_of_vertice;i++)
//        {
//            if (i!=startpoint)
//                {
//                    visited[i]=0;
//                    previous[i]=-1;
//                }
//        }
//
//
//	visited[startpoint]=1;
//	previous[startpoint]=-1;
//	distance_value[startpoint]=0;
//	queue_of_points.push(startpoint);
//}

    void bfs(int aArray[][arraySIZE],int number_of_vertice,int startpoint,int endpoint)
{
    for(int i=0;i<number_of_vertice;i++)
        {
            if (i!=startpoint)
                {
                    visited[i]=0;
                    previous[i]=-1;
                }
        }


	visited[startpoint]=1;
	previous[startpoint]=-1;
	distance_value[startpoint]=0;
	queue_of_points.push(startpoint);

    while (!queue_of_points.empty())
    {
        int u=queue_of_points.front();
        queue_of_points.pop();

        for (int i=0;i<number_of_vertice;i++)
        {
            if (aArray[u][i]!=0)
            {
                int v=i;
                if(visited[v] == 0)
                {
                    visited[v]=1;
                    distance_value[v]=distance_value[u]+1;
                    previous[v]=u;
                    queue_of_points.push(v);


                    if (v==endpoint)
                        {
                            return;
                        }
                }




            }
        }
    }

}



void shortest_path()
{
    startandendpoint();

    if (startpoint< number_of_vertice && endpoint< number_of_vertice)
    {
        bfs(aArray,number_of_vertice,startpoint,endpoint);
        printShortest(startpoint,endpoint);
        //cout<<endl;
        //clearqueue(queue_of_points);
    }
    else
        cout<<"Error: Invalid vertex value detected."<<endl;

 }








void printShortest(int startpoint, int endpoint)
{
    int path[arraySIZE];
    int prev=previous[endpoint];
    int node=0;
    prev=endpoint;

    if (previous[endpoint]==-1)
    {
        cout<<"Error: No Path found between "<<startpoint<<" and "<<endpoint<<"."<<endl;;
        return;
    }


    while (prev!=-1)
    {
        path[node++] = prev;
        prev= previous[prev];
    }

    while (node>0)
    {
        cout<<path[node-1];
        if (node ==1)
        {
            cout<<endl;
        }
        else
        {
            cout<<"-";
        }
        node--;
    }
}





int main()
{

    char c;
    while (cin>>c)
    {
        if(c=='V' || c=='v')
            vertices();
        else if (c=='E' || c=='e')
            add_edge();
        else if (c=='S'||c=='s')
            shortest_path();
        else
            cout<<"Error: Invalid Command."<<endl;
    }


}
