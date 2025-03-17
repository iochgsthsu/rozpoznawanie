if __name__ == '__main__':
	import torch
	import pandas as pd
	import numpy as np
	from matplotlib import pyplot as plt
	from ultralytics import YOLO
	import datetime

	obecna_data = datetime.datetime.now()
	sformatowana_data = obecna_data.strftime("%d%m%Y-%H%M")
	nazwa_pliku =  "yolo_moj_model.pt"

	model = YOLO(nazwa_pliku)
	#device = torch.device('cpu')
	#model.to(device)
	bname = "yolo_moj_model_BACKUP" + sformatowana_data + ".pt"

	print(bname)

	model.save(bname) # tworze backup na wszelki wypadek

	#parametry treningu
	e = 20
	b = 4

	#trening
	model.train(data="dataset.yaml", epochs=e, batch=b)
	#koniec treningu

	model.save(nazwa_pliku) # nadpisuje