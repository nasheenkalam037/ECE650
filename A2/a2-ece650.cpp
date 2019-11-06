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

int check_input();
int vertices();
void add_edge();
int shortest_path();

int matrixInitialize();
int PrintMatrix();
void bfs(int aArray[][arraySIZE],int number_of_vertice,int startpoint,int endpoint);
void initiate_bfs(int startpoint);
void printShortest(int startpoint,int endpoint);
void clearqueue( queue<int> &queue_of_points );

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


int vertices()
{
    cin>>number_of_vertice;
    matrixInitialize();
}


void add_edge()
{
    matrixInitialize();
    char e2;
    int i,j;
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

int matrixInitialize()
    {
        for(i=0;i<100;i++)
            {
                for(j=0;j<100;j++)
                {
                    aArray[i][j] = 0;
                }
            }
    }


int shortest_path()
{
    cin>>startpoint>>endpoint;
    if (startpoint< number_of_vertice && endpoint< number_of_vertice)
    {
        bfs(aArray,number_of_vertice,startpoint,endpoint);
        printShortest(startpoint,endpoint);
        cout<<endl;
        clearqueue(queue_of_points);
    }
    else
        cout<<"Error: Invalid vertex value detected."<<endl;

 }

 void bfs(int aArray[][arraySIZE],int number_of_vertice,int startpoint,int endpoint)
{
    initiate_bfs(startpoint);

    while (!queue_of_points.empty())
    {
        int u=queue_of_points.front();
        queue_of_points.pop();

        for (int v=0;v<number_of_vertice;v++)
        {
            if (aArray[u][v]==1)
            {
                if(visited[v] == 0)
                {
                    visited[v]=1;
                    queue_of_points.push(v);
                    distance_value[v]=u+1;
                    previous[v]=u;
                    if (v==endpoint)
                        {
                            return;
                        }
                }




            }
        }
    }

}

void initiate_bfs(int startpoint)
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
}

void printShortest(int startpoint, int endpoint)
{
    if (endpoint<0)
        return;

    else if (endpoint==startpoint)
    {
        cout<<startpoint;

    }

    else if ((previous[endpoint])==-1)
    {
        cout<<"Error: No Path found between "<<startpoint<<" and "<<endpoint<<".";
        return;
    }

    else
    {
        printShortest(startpoint,previous[endpoint]);
        cout<<"-"<<endpoint;

    }

}

void clearqueue( queue<int> &queue_of_points )
{
  queue<int> empty;
  swap( queue_of_points, empty );
}
