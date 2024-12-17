#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>
#include "lmstruct.h"
#include "lmmin.h"
#include "lmcurve_user.h"
#include "lmmin.c"
#include "lmcurve_user.c"

typedef struct Context {
    double b;
    double c;
    double d;
    double e;
    double f;
} Context;

double N(double C, const double *p, const void *user_data) {
    Context *ctx = (Context *)user_data;

    int pi = 0;
    double b = isnan(ctx->b) ? p[pi++] : ctx->b;
    double c = isnan(ctx->c) ? p[pi++] : ctx->c;
    double d = isnan(ctx->d) ? p[pi++] : ctx->d;
    double e = isnan(ctx->e) ? p[pi++] : ctx->e;
    double f = isnan(ctx->f) ? p[pi++] : ctx->f;

    return c + (d - c) / pow(1 + pow(C / e, b), f);
}

static PyObject *lmcurve_ll5(PyObject *self, PyObject *args) {
    PyObject *x_obj, *y_obj;
    double b, c, d, e, f;

    // Parse input arguments
    if (!PyArg_ParseTuple(args, "O!O!ddddd",
                          &PyList_Type, &x_obj, &PyList_Type, &y_obj,
                          &b, &c, &d, &e, &f)) {
        return NULL;
    }

    // Extract data from Python lists
    Py_ssize_t n = PyList_Size(x_obj);
    double x[n], y[n];
    for (Py_ssize_t i = 0; i < n; i++) {
        x[i] = PyFloat_AsDouble(PyList_GetItem(x_obj, i));
        y[i] = PyFloat_AsDouble(PyList_GetItem(y_obj, i));
    }

    // !!! DATA-FIX, force plateau at x=0
    // Replace x=0 with a very small value
    for (int i = 0; i < n; i++) {
        if (x[i] == 0.0) {
            x[i] = 1.e-100;
        }
    }

    // Set up the context for fixed parameters
    Context ctx = {b, c, d, e, f};
    int pn = 0; // Number of free parameters
    if (isnan(b)) pn++;
    if (isnan(c)) pn++;
    if (isnan(d)) pn++;
    if (isnan(e)) pn++;
    if (isnan(f)) pn++;

    // Initial guesses for free parameters
    double par[5] = {1.0, 1.0, 1.0, 1.0, 1.0};

    // Set up control and status structures
    lm_control_struct control = lm_control_double;
    control.stepbound = 1.e-12;
    control.patience = 1.e+4;
    lm_status_struct status;

    // Run the curve-fitting routine
    lmcurve_user(pn, par, n, x, y, N, &ctx, &control, &status);

    // Reconstruct the parameter array with fixed values
    int pi = 0;
    double final_b = isnan(ctx.b) ? par[pi++] : ctx.b;
    double final_c = isnan(ctx.c) ? par[pi++] : ctx.c;
    double final_d = isnan(ctx.d) ? par[pi++] : ctx.d;
    double final_e = isnan(ctx.e) ? par[pi++] : ctx.e;
    double final_f = isnan(ctx.f) ? par[pi++] : ctx.f;

    // Return the final parameters as a tuple
    return Py_BuildValue("ddddd", final_b, final_c, final_d, final_e, final_f);
}


// Module method table
static PyMethodDef RlmcurveMethods[] = {
    {"lmcurve_ll5", lmcurve_ll5, METH_VARARGS, "Curve fitting function."},
    {NULL, NULL, 0, NULL}  // Sentinel
};

// Module definition
static struct PyModuleDef lmcurve_ll5module = {
    PyModuleDef_HEAD_INIT,
    "lmcurve_ll5",
    "Python wrapper for curve fitting using lmcurve.",
    -1,
    RlmcurveMethods
};

// Module initialization
PyMODINIT_FUNC PyInit_lmcurve_ll5(void) {
    return PyModule_Create(&lmcurve_ll5module);
}
