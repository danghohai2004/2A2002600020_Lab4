 
# ============================================================
# TravelBuddy - Trợ lý Du Lịch Thông Minh
# Gõ 'quit' để thoát
# ============================================================

# Test case 1:

Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

TravelBuddy đang suy nghĩ...

Trả lời trực tiếp

TravelBuddy: Chào bạn! Thật tuyệt vời khi bạn đang có kế hoạch đi du lịch. Bạn có định đi vào thời gian nào và ngân sách của bạn khoảng bao nhiêu không? Nếu có đích đến nào trong đầu, hay bạn muốn gợi ý nghỉ dưỡng vài nơi đẹp ở Việt Nam, hãy cho mình biết nhé! 😊

# Test case 2:
Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...

Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})

Trả lời trực tiếp

TravelBuddy: Wow, có nhiều lựa chọn cho chuyến bay từ Hà Nội đi Đà Nẵng đấy! Dưới đây là thông tin chi tiết:

**Chuyến bay:**
1. **VietJet Air** (economy): 08:30 -> 09:50 | Giá: 890,000đ
2. **Bamboo Airways** (economy): 11:00 -> 12:20 | Giá: 1,200,000đ
3. **Vietnam Airlines** (economy): 06:00 -> 07:20 | Giá: 1,450,000đ
4. **Vietnam Airlines** (business): 14:00 -> 15:20 | Giá: 2,800,000đ

Nếu bạn cần hỗ trợ thêm về khách sạn hoặc các hoạt động khác tại Đà Nẵng, hãy cho mình biết nhé! 🏖️✈️

# Test case 3:
Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

TravelBuddy đang suy nghĩ...

Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})

Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1750000})

Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 'flight:1350000,hotel:2400000'})

Trả lời trực tiếp

TravelBuddy: Đã tìm xong cho bạn chuyến bay và khách sạn phù hợp rồi nè!

**Chuyến bay:**
- VietJet Air (economy): 10:00 -> 12:15 | Giá: 1.350.000đ

**Khách sạn:**
- 9Station Hostel (⭐⭐): Khu vực Dương Đông, giá: 200.000đ/đêm.
- Bạn sẽ ở 2 đêm, tổng cộng là 400.000đ.

**Tổng chi phí ước tính:**
- Vé máy bay: 1.350.000đ
- Khách sạn (2 đêm): 400.000đ
- **Tổng cộng: 1.750.000đ**

Còn lại ngân sách cho bạn là 5.000.000đ - 1.750.000đ = 3.250.000đ!

**Gợi ý thêm:**
Bạn có thể sử dụng số tiền còn lại để thưởng thức ẩm thực, tham gia các hoạt động vui chơi hay mua sắm tại Phú Quốc. Nếu cần thêm thông tin hay gợi ý gì nữa, cứ hỏi nhé! Chúc bạn có chuyến đi vui vẻ! 🌴🌊

# Test case 4:
Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...

Trả lời trực tiếp

TravelBuddy: Ôi, tuyệt quá! Bạn đang tìm đặt khách sạn ở đâu vậy? Và bạn có ngân sách dự kiến khoảng bao nhiêu mỗi đêm không? Thông tin này sẽ giúp mình tư vấn chính xác hơn cho bạn.

# Test case 5:
Bạn: Giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...

Trả lời trực tiếp

TravelBuddy: Xin lỗi, nhưng mình chỉ có thể giúp bạn với các thông tin liên quan đến du lịch thôi. Nếu bạn cần tư vấn về chuyến đi hoặc điểm đến nào đó, hãy cho mình biết nhé!
