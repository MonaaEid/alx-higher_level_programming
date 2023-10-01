#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p)
{
	PyUnicodeObject *pyUnicode = (PyUnicodeObject *) p;

	if (!PyUnicode_Check(pyUnicode))
	{
		fprintf(stderr, "TypeError: print_python_string() argument must be a string\n");
		return;
	}
	printf("  %.*s", (int) PyUnicode_GET_LENGTH(pyUnicode), PyUnicode_AsUTF8(pyUnicode));
	printf("\n");
}
