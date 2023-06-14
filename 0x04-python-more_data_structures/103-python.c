#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints Python lists information
 * @p: Pointer to the Python object.
 *
 * Return: Void.
 */

void print_python_list(PyObject *p)
{
	int i, l_size, allocate;
	PyListObject *plist = (PyListObject *)p;
	PyVarObject *pvar = (PyVarObject *)p;
	const char *type;

	l_size = pvar->ob_size;
	allocate = plist->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", l_size);
	printf("[*] Allocated = %d\n", allocate);

	for (i = 0; i < l_size; i++)
	{
		type = plist->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(plist->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints Python bytes information
 * @p: Pointer to the Python object.
 *
 * Return: void.
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned char i, l_size;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		l_size = 10;
	else
		l_size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", l_size);
	for (i = 0; i < l_size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (l_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
