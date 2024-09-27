import os
import re
import tarfile

def tardump(field, data_list, labels = None):
  tnam = re.sub(r"[^a-zA-Z0-9_]+", "_", field).strip('_')
  with tarfile.open(f'{tnam}.tar.xz', 'w:xz') as tar:
    if labels is None: iteratee = zip(data_list, [str(x.name) for x in data_list])
    else: iteratee = zip(data_list, labels)
    for data, name in iteratee:
      anam = re.sub(r"[^a-zA-Z0-9_]+", "_", name).strip('_')
      fnam = f'{anam}.csv'
      data.to_csv(fnam)
      tar.add(fnam, arcname = f'{tnam}/{anam}.csv')
      os.remove(fnam)
