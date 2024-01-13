num_guests = int(input())
codes = set()
for _ in range(num_guests):
    code = input()
    codes.add(code)
while True:
    guest_code = input()
    if guest_code == "END":
        break
    elif guest_code in codes:
        codes.remove(guest_code)

non_attending_guests = len(codes)
print(non_attending_guests)

codes = sorted(codes)
for code in codes:
    print(code)
