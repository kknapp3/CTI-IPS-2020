def distribute_content(cdns, requests):
    image_locations, image_requests = [], {}
    for request in requests:
        image_name = request['path'].split('.')[0]
        origin = [float(request['ip'].split('.')[0]) + float(request['ip'].split('.')[1]) / 1000]
        image_requests[image_name] = image_requests[image_name] + origin if image_name in image_requests else origin
    for k,v in image_requests.items():
        mn, mn_pos = abs(sum(v)/len(v) - (float(cdns[0].split('.')[0]) + float(cdns[0].split('.')[1]) / 1000)), 0
        for i,server in enumerate(cdns):
            prox = abs(sum(v)/len(v) - (float(server.split('.')[0]) + float(server.split('.')[1]) / 1000))
            if prox < mn:
                mn, mn_pos = prox, i
        image_locations.append({'image': k, 'server': cdns[mn_pos]})
    return image_locations

content_distribution_network_ips = ["4.2.5.66", "5.8.94.12", "14.9.144.56", "94.94.112.4", "200.8.8.90"]
requests = [
  {
    "path": "image_02309.jpg",
    "ip": "4.4.5.6"
  },
  {
    "path": "image_8899.jpg",
    "ip": "15.9.3.8"
  },
  {
    "path": "image_34095.jpg",
    "ip": "95.14.55.11"
  },
  {
    "path": "image_34095.jpg",
    "ip": "92.11.44.112"
  }
]
print(distribute_content(content_distribution_network_ips, requests))