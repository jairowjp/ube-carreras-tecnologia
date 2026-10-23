# Carreras de tecnología · UBE

Sitio interactivo para promocionar entre bachilleres las carreras en línea de la Universidad Bolivariana del Ecuador:

- **Ingeniería en Sistemas Inteligentes**
- **Ingeniería en Inteligencia Artificial y Ciberseguridad**

Incluye: hero animado (red neuronal), ficha de cada carrera, malla curricular interactiva (43 asignaturas por carrera, filtros por unidad, detalle de horas y contenidos), test vocacional, sección de modalidad y titulación, y música de fondo original generada en el navegador con Tone.js.

## Estructura

```
index.html          Página completa (HTML + CSS + JS, autocontenida)
app.py              App de Streamlit que sirve index.html a pantalla completa
requirements.txt
.streamlit/config.toml
assets/             Coloca aquí logo.png (o .svg/.jpg/.webp)
```

## Ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

También puedes abrir `index.html` directamente en el navegador.

## Editar las mallas

Los datos están en `index.html`, en la constante `MALLAS` (una lista por periodo).
Cada asignatura tiene: `n` nombre, `u` unidad (`b` básica, `p` profesional, `i` integración),
`h` horas, `f` frase para estudiantes, `o` temas oficiales (opcional),
`psc` / `pl` horas de prácticas (opcional) e `it` opciones de itinerario (opcional).

## Publicar en Streamlit Community Cloud

1. Sube este repositorio a GitHub.
2. Entra a https://share.streamlit.io, elige **Create app** → repositorio, rama `main`, archivo `app.py`.
3. Pulsa **Deploy**.

## Música

La música es una composición original generada en tiempo real con Tone.js (sin archivos de audio ni derechos de terceros).
Los navegadores bloquean el audio automático, por eso empieza con el primer toque o clic del visitante. El botón **Música** la pausa y recuerda la preferencia.
