# ProjectMakerSpace

ProjectMakerSpace es un proyecto de código abierto para gestionar proyectos de software.

ProjectMakerSpace is an open source project for managing software projects.

## Estado

En desarrollo. La funcionalidad todavía no está definida.

In development. The features are not defined yet.

## Ejecutar con Docker

```powershell
docker compose up --build -d
```

- Web: http://localhost:3001
- API: http://localhost:3002

## Ejecutar sin Docker

```powershell
# API (ProjectMakerSpaceApi), puerto 3002
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Web (ProjectMakerSpaceWeb), puerto 3001
npm install
npm run dev
```

## Módulos

- Organizador Kanban: tableros, listas y tarjetas.

## Licencia

ProjectMakerSpace se distribuye bajo la [licencia MIT](LICENSE) (`MIT`). Puedes usar, copiar, modificar y distribuir el código, incluso con fines comerciales, siempre que conserves el aviso de copyright y el texto de la licencia. El software se entrega "tal cual", sin garantía de ningún tipo.

Los componentes de terceros (Django, Django REST Framework, Next.js, React y las demás dependencias) conservan sus propias licencias.

## License

ProjectMakerSpace is licensed under the [MIT License](LICENSE) (`MIT`). You may use, copy, modify and distribute the code, including for commercial purposes, as long as you keep the copyright notice and the license text. The software is provided "as is", without warranty of any kind.

Third-party components (Django, Django REST Framework, Next.js, React and the other dependencies) remain subject to their own licenses.
