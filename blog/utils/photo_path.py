def get_photo_path(instance, filename: str) -> str:
    object_id = getattr(instance, 'id', None)
    
    # katalog: nazwa_modelu/id/nazwa_pliku.jpg
    return "{}/{}/{}".format(
		instance.__class__.__name__.lower(),
		object_id,
		filename
	)
    