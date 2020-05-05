import json
import pickle
from time import time

lorem_example = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a,'

lorem = [lorem_example.split()] * 100000

start = time()

pickled = pickle.dumps(lorem)

pickle.loads(pickled)

end = time()

print(end - start)  # 0.004999637603759766

start = time()

jsonX = json.dumps(lorem)

json.loads(jsonX)

end = time()

print(end - start)  # 2.725743293762207