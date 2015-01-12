import segment

class DanielSegmentation(segment.SegmentationStrategy):
    def __init__(self, params):
        pass  # set your parameters here

    def find_centers(self, dataset):
        slice_dataset = dataset[:,  # sequences
                                :,  # frames
                                :,  # planes
				:20,  # first 20 rows
                                :20,  # first 20 columns
                                ]
	array_of_first_sequence = np.array(
            dataset.sequences[0])
                               
        for sequence in dataset:
            for frame in sequence:
                # frame is a numpy.array (zyx-channel)
                frame[:, :, :, 0]  # get the first channel
                frame[:, :, :, 1]  # get the second channel
                for plane in frame:
                    for row in plane:
                        for pixel in row
                            for channel in pixel
                         

    def segment(self, dataset):
        centers = self.find_centers(dataset)
        result = nnmf(dataset, centers)
        return result

