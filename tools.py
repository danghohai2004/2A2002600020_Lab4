from langchain_core.tools import tool

FLIGHTS_DB = {
    "Hà Nội - Đà Nẵng": [
        {
            "airline": "Vietnam Airlines",
            "departure": "06:00",
            "arrival": "07:20",
            "price": 1450000,
            "class": "economy",
        },
        {
            "airline": "Vietnam Airlines",
            "departure": "14:00",
            "arrival": "15:20",
            "price": 2800000,
            "class": "business",
        },
        {
            "airline": "VietJet Air",
            "departure": "08:30",
            "arrival": "09:50",
            "price": 890000,
            "class": "economy",
        },
        {
            "airline": "Bamboo Airways",
            "departure": "11:00",
            "arrival": "12:20",
            "price": 1200000,
            "class": "economy",
        },
    ],
    "Hà Nội - Phú Quốc": [
        {
            "airline": "Vietnam Airlines",
            "departure": "07:00",
            "arrival": "09:15",
            "price": 2100000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "10:00",
            "arrival": "12:15",
            "price": 1350000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "16:00",
            "arrival": "18:15",
            "price": 1100000,
            "class": "economy",
        },
    ],
    "Hà Nội - Hồ Chí Minh": [
        {
            "airline": "Vietnam Airlines",
            "departure": "06:00",
            "arrival": "08:10",
            "price": 1600000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "07:30",
            "arrival": "09:40",
            "price": 950000,
            "class": "economy",
        },
        {
            "airline": "Bamboo Airways",
            "departure": "12:00",
            "arrival": "14:10",
            "price": 1300000,
            "class": "economy",
        },
        {
            "airline": "Vietnam Airlines",
            "departure": "18:00",
            "arrival": "20:10",
            "price": 3200000,
            "class": "business",
        },
    ],
    "Hồ Chí Minh - Đà Nẵng": [
        {
            "airline": "Vietnam Airlines",
            "departure": "09:00",
            "arrival": "10:20",
            "price": 1300000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "13:00",
            "arrival": "14:20",
            "price": 780000,
            "class": "economy",
        },
    ],
    "Hồ Chí Minh - Phú Quốc": [
        {
            "airline": "Vietnam Airlines",
            "departure": "08:00",
            "arrival": "09:00",
            "price": 1100000,
            "class": "economy",
        },
        {
            "airline": "VietJet Air",
            "departure": "15:00",
            "arrival": "16:00",
            "price": 650000,
            "class": "economy",
        },
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {
            "name": "Mường Thanh Luxury",
            "stars": 5,
            "price_per_night": 1800000,
            "area": "Mỹ Khê",
            "rating": 4.5,
        },
        {
            "name": "Sala Danang Beach",
            "stars": 4,
            "price_per_night": 1200000,
            "area": "Mỹ Khê",
            "rating": 4.3,
        },
        {
            "name": "Fivitel Danang",
            "stars": 3,
            "price_per_night": 650000,
            "area": "Sơn Trà",
            "rating": 4.1,
        },
        {
            "name": "Memory Hostel",
            "stars": 2,
            "price_per_night": 250000,
            "area": "Hải Châu",
            "rating": 4.6,
        },
        {
            "name": "Christina's Homestay",
            "stars": 2,
            "price_per_night": 350000,
            "area": "An Thượng",
            "rating": 4.7,
        },
    ],
    "Phú Quốc": [
        {
            "name": "Vinpearl Resort",
            "stars": 5,
            "price_per_night": 3500000,
            "area": "Bãi Dài",
            "rating": 4.4,
        },
        {
            "name": "Sol by Meliá",
            "stars": 4,
            "price_per_night": 1500000,
            "area": "Bãi Trường",
            "rating": 4.2,
        },
        {
            "name": "Lahana Resort",
            "stars": 3,
            "price_per_night": 1200000,
            "area": "Dương Đông",
            "rating": 4.5,
        },
        {
            "name": "9Station Hostel",
            "stars": 2,
            "price_per_night": 200000,
            "area": "Dương Đông",
            "rating": 4.5,
        },
    ],
    "Hồ Chí Minh": [
        {
            "name": "Rex Hotel",
            "stars": 5,
            "price_per_night": 2800000,
            "area": "Quận 1",
            "rating": 4.3,
        },
        {
            "name": "Liberty Central",
            "stars": 4,
            "price_per_night": 1400000,
            "area": "Quận 1",
            "rating": 4.1,
        },
        {
            "name": "Cochin Zen Hotel",
            "stars": 3,
            "price_per_night": 550000,
            "area": "Quận 3",
            "rating": 4.4,
        },
        {
            "name": "The Common Room",
            "stars": 2,
            "price_per_night": 180000,
            "area": "Quận 1",
            "rating": 4.6,
        },
    ],
}


@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.
    Tham số:
    - origin: thành phố khởi hành (VD: 'Hà Nội', 'Hồ Chí Minh')
    - destination: thành phố đến (VD: 'Đà Nẵng', 'Phú Quốc')
    Trả về danh sách chuyến bay với hãng, giờ bay, giá vé.
    Nếu không tìm thấy tuyến bay, trả về thông báo không có chuyến.
    """
    route = (origin, destination)
    reverse_route = (destination, origin)

    route_key = f"{route[0]} - {route[1]}"
    reverse_key = f"{reverse_route[0]} - {reverse_route[1]}"

    flights = FLIGHTS_DB.get(route_key)

    if not flights:
        if FLIGHTS_DB.get(reverse_key):
            return f"Hiện tại không có chuyến từ {origin} đến {destination}, nhưng có chuyến chiều ngược lại. Bạn có muốn tham khảo không?"
        return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."

    result_lines = [f"Danh sách chuyến bay từ {origin} đến {destination}:"]

    for f in flights:
        formatted_price = "{:,.0f}đ".format(f["price"]).replace(",", ".")

        line = (
            f"- {f['airline']} ({f['class']}): {f['departure']} -> {f['arrival']} "
            f"| Giá: {formatted_price}"
        )
        result_lines.append(line)

    return "\n".join(result_lines)


@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.
    Tham số:
    - city: tên thành phố (VD: 'Đà Nẵng', 'Phú Quốc', 'Hồ Chí Minh')
    - max_price_per_night: giá tối đa mỗi đêm (VNĐ), mặc định không giới hạn
    Trả về danh sách khách sạn phù hợp với tên, số sao, giá, khu vực, rating.
    """

    hotels = HOTELS_DB.get(city)

    if not hotels:
        return f"Hiện tại TravelBuddy chưa có dữ liệu khách sạn tại {city}."

    filtered_hotels = [h for h in hotels if h["price_per_night"] <= max_price_per_night]

    filtered_hotels.sort(key=lambda x: x["rating"], reverse=True)

    if not filtered_hotels:
        formatted_max_price = "{:,.0f}".format(max_price_per_night).replace(",", ".")
        return (
            f"Không tìm thấy khách sạn tại {city} với giá dưới {formatted_max_price}đ/đêm. "
            f"Hãy thử tăng ngân sách để có thêm lựa chọn nhé."
        )

    result_lines = [
        f"Dưới đây là các khách sạn tại {city} (Ưu tiên đánh giá cao nhất):"
    ]

    for h in filtered_hotels:
        price = "{:,.0f}đ".format(h["price_per_night"]).replace(",", ".")
        stars = "⭐" * h["stars"]

        line = (
            f"- {h['name']} ({stars}) | Khu vực: {h['area']} "
            f"| Rating: {h['rating']}/5 | Giá: {price}/đêm"
        )
        result_lines.append(line)

    return "\n".join(result_lines)


@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách du lịch.

    Tham số:
    - total_budget: tổng ngân sách (VNĐ)
    - expenses: danh sách chi phí dạng "tên:số, tên:số"

    Ví dụ:
    "flight:1200000,hotel:800000,food:300000"

    Trả về bảng chi phí và số tiền còn lại.
    """

    try:
        expense_list = expenses.split(",")
        expense_dict = {}
        total_expense = 0

        for item in expense_list:
            if ":" not in item:
                return (
                    "Lỗi format: Mỗi khoản chi phải có định dạng 'tên_khoản:số_tiền'."
                )

            name, amount = item.split(":")
            amount = int(amount.strip())
            expense_dict[name.strip()] = amount
            total_expense += amount

        remaining = total_budget - total_expense

        def fmt(val):
            return "{:,.0f}đ".format(val).replace(",", ".")

        result = ["Bảng chi phí:"]
        for name, amount in expense_dict.items():
            result.append(f"- {name}: {fmt(amount)}")

        result.append("---")
        result.append(f"Tổng chi: {fmt(total_expense)}")
        result.append(f"Ngân sách: {fmt(total_budget)}")

        if remaining >= 0:
            result.append(f"Còn lại: {fmt(remaining)}")
        else:
            result.append(f"Vượt ngân sách {fmt(abs(remaining))}! Cần điều chỉnh.")

        return "\n".join(result)

    except ValueError:
        return "Lỗi: Số tiền trong danh sách chi phí phải là con số hợp lệ."
    except Exception as e:
        return f"Đã xảy ra lỗi không xác định: {str(e)}"
