#include "binary_trees.h"

size_t binary_tree_size(const binary_tree_t *tree){
	size_t size;
	if (!tree)
		return (0);
	size = 1 + binary_tree_size(tree->left) + binary_tree_size(tree->right);
	return (size);
}

char *numtostr(unsigned long int num, int base){
	static char *repre, buff[50];
	char *binary;

	repre = "01";

	binary = &buff[49];
	*binary = 0;
	while (num)
	{
		binary--;
		*binary = repre[num % base];
		num /= base;
	}
	return (binary);
}

void insert_node(heap_t **root, heap_t *node){
	char bin, *binary;
	unsigned int idx, size;
	heap_t *aux = NULL;

	aux = *root;
	size = binary_tree_size(aux) + 1;
	binary = numtostr(size, 2);
	for (idx = 1; idx < strlen(binary); idx++)
	{
		bin = binary[idx];
		if (idx == strlen(binary) - 1)
		{
			if (bin == '1')
				aux->right = node;
			if (bin == '0')
				aux->left = node;
			node->parent = aux;
		}
		else if (bin == '1')
			aux = aux->right;
		else if (bin == '0')
			aux = aux->left;
	}
}

heap_t *heap_insert(heap_t **root, int value){
	heap_t *new_node = NULL;
	int n;

	if (!root)
		return (NULL);
	new_node = binary_tree_node(NULL, value);
	if (!(*root))
	{
		*root = new_node;
		return (new_node);
	}
	insert_node(root, new_node);
	while (new_node->parent && new_node->n > new_node->parent->n)
	{
		n = new_node->parent->n;
		new_node->parent->n = new_node->n;
		new_node->n = n;
		new_node = new_node->parent;
	}
	return (new_node);
}
