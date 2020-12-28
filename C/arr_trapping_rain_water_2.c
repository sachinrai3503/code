// https://leetcode.com/problems/trapping-rain-water-ii
/*
Given an m x n matrix of positive integers representing the height of each unit 
cell in a 2D elevation map, compute the volume of water it is able to trap after
 raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

Constraints:

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000
*/


#include <malloc.h>
#include <stdio.h>
#include <limits.h>

void print_arr(int *ip, int length)
{
    int i = 0;
    for (; i < length; i++)
    {
        printf("%d ", ip[i]);
    }
    printf("\n");
}

void print_2d(int **ip, int row, int col)
{
    int i = 0;
    for (; i < row; i++)
    {
        print_arr(ip[i], col);
    }
}

int **init_2d_arr(int row, int col)
{
    int **arr = (int **)calloc(row, sizeof(int *));
    int i = 0;
    for (; i < row; i++)
    {
        arr[i] = (int *)calloc(col, sizeof(int));
    }
    return arr;
}

typedef struct
{
    int i, j;
} heap_node;

typedef struct
{
    int **ip;
    heap_node **data;
    int max_size, cur_size;
} heap;

heap_node *init_heap_node(int i, int j)
{
    heap_node *node = (heap_node *)malloc(sizeof(heap_node));
    if (node)
    {
        node->i = i;
        node->j = j;
    }
    return node;
}

heap *init_heap(int **heightMap, int max_size)
{
    heap *_heap = (heap *)malloc(sizeof(heap));
    if (_heap)
    {
        _heap->ip = heightMap;
        _heap->data = (heap_node **)calloc(max_size, sizeof(heap_node));
        _heap->max_size = max_size;
        _heap->cur_size = 0;
    }
    return _heap;
}

void swap(heap_node **a, heap_node **b)
{
    heap_node *temp = *a;
    *a = *b;
    *b = temp;
}

void min_heapify(heap *_heap, int index)
{
    int left = index * 2 + 1;
    int right = index * 2 + 2;
    int min_index = index;
    if (left < _heap->cur_size && _heap->ip[_heap->data[left]->i][_heap->data[left]->j] < _heap->ip[_heap->data[min_index]->i][_heap->data[min_index]->j])
    {
        min_index = left;
    }
    if (right < _heap->cur_size && _heap->ip[_heap->data[right]->i][_heap->data[right]->j] < _heap->ip[_heap->data[min_index]->i][_heap->data[min_index]->j])
    {
        min_index = right;
    }
    if (min_index != index)
    {
        swap(_heap->data + index, _heap->data + min_index);
        min_heapify(_heap, min_index);
    }
}

int is_empty(heap *_heap)
{
    if (_heap->cur_size == 0)
        return 1;
    return 0;
}

int is_full(heap *_heap)
{
    if (_heap->cur_size == _heap->max_size)
        return 1;
    return 0;
}

void insert_heap(heap *_heap, int i, int j)
{
    if (is_full(_heap))
    {
        printf("Full\n");
        return;
    }
    heap_node *node = init_heap_node(i, j);
    _heap->data[_heap->cur_size++] = node;
    int parent_index = (_heap->cur_size - 2) / 2;
    for (; parent_index > 0; parent_index = (parent_index - 1) / 2)
    {
        min_heapify(_heap, parent_index);
    }
    if (parent_index == 0)
    {
        min_heapify(_heap, parent_index);
    }
}

heap_node *delete_top(heap *_heap)
{
    if (is_empty(_heap))
    {
        printf("Empty\n");
        return NULL;
    }
    heap_node *temp = _heap->data[0];
    _heap->data[0] = _heap->data[--_heap->cur_size];
    min_heapify(_heap, 0);
    return temp;
}

void print_heap(heap *_heap)
{
    int i = 0;
    for (; i < _heap->cur_size; i++)
    {
        printf("(%d-%d) <> ", _heap->data[i]->i, _heap->data[i]->j);
    }
    printf("\n");
}

void insert_boundary_cells(heap *_heap, int row, int col, int **visited)
{
    int i = 0;
    for (; i < col; i++)
    {
        insert_heap(_heap, 0, i);
        insert_heap(_heap, row - 1, i);
        visited[0][i] = visited[row - 1][i] = 1;
    }
    for (i = 1; i < row - 1; i++)
    {
        insert_heap(_heap, i, 0);
        insert_heap(_heap, i, col - 1);
        visited[i][col - 1] = visited[i][0] = 1;
    }
}

int is_valid(int row, int col, int **visited, int i, int j)
{
    if (i < 0 || i >= row || j < 0 || j >= col)
        return 0;
    if (visited[i][j] == 1)
        return 0;
    return 1;
}

int trapRainWater(int **heightMap, int heightMapSize, int *heightMapColSize)
{
    int res = 0;
    if (heightMapSize <= 0 || *heightMapColSize <= 0)
    {
        printf("Empty\n");
        return 0;
    }
    int adj[2][4] = {{0, -1, 0, 1}, {-1, 0, 1, 0}};
    int max = INT_MIN;
    int **visited = init_2d_arr(heightMapSize, *heightMapColSize);
    // print_2d(visited, heightMapSize, *heightMapColSize);
    heap *_heap = init_heap(heightMap, heightMapSize * (*heightMapColSize));
    insert_boundary_cells(_heap, heightMapSize, *heightMapColSize, visited);
    // print_2d(visited, heightMapSize, *heightMapColSize);
    // print_heap(_heap);
    while (!is_empty(_heap))
    {
        heap_node *temp = delete_top(_heap);
        if (heightMap[temp->i][temp->j] > max)
            max = heightMap[temp->i][temp->j];
        int i = 0;
        for (; i < 4; i++)
        {
            int ti = temp->i + adj[0][i];
            int tj = temp->j + adj[1][i];
            if (is_valid(heightMapSize, *heightMapColSize, visited, ti, tj))
            {
                insert_heap(_heap, ti, tj);
                visited[ti][tj] = 1;
                if (heightMap[ti][tj] < max)
                    res = res + (max - heightMap[ti][tj]);
            }
        }
    }
    return res;
}