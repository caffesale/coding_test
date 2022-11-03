// c언어와 인접 리스트로 구현한 Graph 구조

#ifndef GRAPH_H
#define GRAPH_H

#include <stdio.h>
#include <stdlib.h>

enum VisitMode { Visited, NotVisited };

typedef int ElementType;

// 정점은 
// Data, 정점 번호를 뜻하는 Index, 방문 여부를 나타내는 Visited,
// 다음 정점은 가리키는 Next 포인터, 인접 정점의 목록에 대한 포인터 AdjacencyList를 가진다.


typedef struct tagVertex {
  ElementType Data;
  int Visited;
  int Index;

  struct tagVertex* Next;
  struct tagEdge* AdjacencyList;
}

// 간선은 
// 가중치 Weight, 다음 간선을 가리키는 Next
// 시작과 끝 정점 From, Target로 구성된다.

typedef struct tagEdge {
  int Weight;
  struct tagEdge* Next;
  Vertex* From;
  Vertex* Target;
} Edge;

// 그래프는
// 정점 목록에 대한 포인터 Vertices, 
// 정점 수를 나타내는 VertexCount를 가진다.

typedef struct tagGraph {
  vertex* Vertices;
  int VertexCount;
} Graph;