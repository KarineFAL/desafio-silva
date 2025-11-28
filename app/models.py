from django.db import models

class Biome(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Bioma"
        verbose_name_plural = "Biomas"

    def __str__(self):
        return self.name


class Tree(models.Model):
    common_name = models.CharField(max_length=150)
    scientific_name = models.CharField(max_length=200)
    biomes = models.ManyToManyField(Biome, related_name="trees")
    description = models.TextField()

    class Meta:
        verbose_name = "Árvore"
        verbose_name_plural = "Árvores"

    def __str__(self):
        return self.common_name


class TreeBiome(models.Model):
    tree = models.ForeignKey(
        Tree,
        on_delete=models.CASCADE,
        related_name="tree_biomes"
    )
    biome = models.ForeignKey(
        Biome,
        on_delete=models.CASCADE,
        related_name="biome_trees"
    )

    class Meta:
        db_table = "tree_biomes"
        unique_together = ("tree", "biome")
        verbose_name = "Árvore por Bioma"
        verbose_name_plural = "Árvores por Bioma"

    def __str__(self):
        return f"{self.tree.common_name} → {self.biome.name}"
