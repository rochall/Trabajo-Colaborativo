# ==============================================================================
# PROYECTO RSTUDIO: ANÁLISIS DE CALIDAD DE VINOS
# OBJETIVO: Cargar datos desde un CSV y generar 3 gráficos profesionales y detallados.
# ==============================================================================

# 1. INSTALACIÓN Y CARGA DE LIBRERÍAS
# (Si no las tienes instaladas, descomenta las siguientes dos líneas)
# install.packages("tidyverse")
# install.packages("GGally")

library(tidyverse)
install.packages("GGally") # Para la matriz de correlación avanzada
library(GGally)
# 2. LECTURA DE LOS DATOS
# Explicación: read_csv de tidyverse asume por defecto que el separador es la coma (,)
# REEMPLAZA 'nombre_de_tu_archivo.csv' por la ruta o nombre real de tu archivo.
tryCatch({
  df <- read_csv("calidad_de_vino.csv")
  print("¡Datos cargados correctamente en RStudio!")
}, error = function(e) {
  print("Error: No se encontró el archivo. Asegúrate de configurar tu directorio de trabajo.")
})

# Convertimos la variable 'calidad' a factor para mejorar la visualización en los gráficos 1 y 2
df$calidad_factor <- as.factor(df$calidad)


# ==============================================================================
# GRÁFICO 2: Relación entre Alcohol y pH con Impacto en la Calidad
# (Gráfico de dispersión con degradado continuo de color)
# ==============================================================================

grafico2 <- ggplot(df, aes(x = alcohol, y = pH, color = calidad)) +
  geom_point(aes(size = calidad), alpha = 0.75) +
  scale_color_viridis_c(option = "viridis", name = "Calidad (Num)") +
  scale_size_continuous(guide = "none") + # Oculta la leyenda del tamaño para no saturar
  labs(
    title = "Análisis Químico: Relación entre Grado Alcohólico, pH y Calidad",
    subtitle = "El tamaño y color de los puntos representan la calificación del vino",
    x = "Contenido de Alcohol (% vol)",
    y = "Nivel de pH (Acidez del Entorno)"
  ) +
  theme_light() +
  theme(
    plot.title = element_text(face = "bold", size = 14, color = "#333333"),
    plot.subtitle = element_text(size = 10, color = "#666666", face = "italic"),
    axis.title.x = element_text(margin = margin(t = 10)),
    axis.title.y = element_text(margin = margin(r = 10)),
    legend.position = "right"
  )

print(grafico2)
ggsave("grafico_2_alcohol_ph.png", plot = grafico2, width = 8, height = 5, dpi = 300)


