#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type);

        if (strcmp(type, "bytes") == 0)
            print_python_bytes(item);
    }
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    unsigned char *data = (unsigned char *)bytes->ob_sval;

    printf("[.] bytes object info\n");
    if (strcmp(Py_TYPE(p)->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", data);

    Py_ssize_t print_size = (size > 10) ? 10 : size;

    printf("  first %zd bytes: ", print_size);
    for (i = 0; i < print_size; i++)
    {
        printf("%02hhx", data[i]);
        if (i == (print_size - 1))
            printf("\n");
        else
            printf(" ");
    }
}

