# given a log of requests for the images over last month, and the regions you have a server in. Write a function that will determine which regions to host the image in.
# 
# To determine which region an image will need to be located in, look at the first two numbers in the IP block. Assume that locating images in the closest IP block to the request will suffice for geographic relevance.
# 
# Return an array of dictionaries that have the image's name, and the server they should go on.


def distribute_content(cdns, requests):
    image_locations, image_requests = [], {}
    for request in requests:   # set up a dictionary with the image filenames as keys, and store the ip of every request as values
        image_name = request['path'].split('.')[0]
        origin = [float(request['ip'].split('.')[0]) + float(request['ip'].split('.')[1]) / 1000]
        image_requests[image_name] = image_requests[image_name] + origin if image_name in image_requests else origin
    for k,v in image_requests.items():   # now iterate thru the dictionary and calculate the 'average' of the requesting ip's for each image
        mn, mn_pos = abs(sum(v)/len(v) - (float(cdns[0].split('.')[0]) + float(cdns[0].split('.')[1]) / 1000)), 0
        for i,server in enumerate(cdns):   # then iterate thru the server ip's and find the one with the ip closest to the 'average' requesting ip
            prox = abs(sum(v)/len(v) - (float(server.split('.')[0]) + float(server.split('.')[1]) / 1000))
            if prox < mn:
                mn, mn_pos = prox, i
        image_locations.append({'image': k, 'server': cdns[mn_pos]})  # set up the image and selected server in a new dictionary with the
    return image_locations                                            #  specified format and store it in the final list to be returned

content_distribution_network_ips = [ "4.2.5.66", "5.8.94.12", "14.9.144.56", "94.94.112.4", "200.8.8.90" ]

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
