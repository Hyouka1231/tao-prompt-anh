import streamlit as st

st.set_page_config(page_title="Công cụ Tạo Prompt Ảnh", layout="wide")

# Thiết lập chìa khóa khởi tạo để nút Xóa thông tin hoạt động 100%
if "reset_key" not in st.session_state:
    st.session_state.reset_key = 0

if "edit_items" not in st.session_state:
    st.session_state.edit_items = [{"element": "", "level": "Không thay đổi"}]
    
if "merge_images" not in st.session_state:
    st.session_state.merge_images = ["Ảnh 1", "Ảnh 2"]

# Hàm reset toàn bộ dữ liệu (Sử dụng mẹo đổi key để ép Streamlit làm mới)
def xoa_toan_bo():
    try:
        st.session_state.reset_key += 1
        st.session_state.edit_items = [{"element": "", "level": "Không thay đổi"}]
        st.session_state.merge_images = ["Ảnh 1", "Ảnh 2"]
    except Exception as e:
        st.error(f"Có lỗi nhỏ khi xóa dữ liệu: {e}")

# --- KHO DỮ LIỆU KHỔNG LỒ ---
chu_the_opts = [
    "Không chọn",
    "Cô gái trẻ", "Chàng trai thanh niên", "Ông lão râu tóc bạc phơ", "Bà lão hiền từ", "Em bé bụ bẫm", 
    "Nữ chiến binh", "Phi hành gia", "Phù thủy", "Hiệp sĩ mặc giáp", "Ninja sát thủ", "Bác sĩ", 
    "Cảnh sát", "Ca sĩ đang hát", "Vũ công", "Samurai", "Thợ lặn", "Điệp viên", "Vua/Nữ hoàng", 
    "Người mẫu thời trang", "Thợ rèn vạm vỡ", "Nhà khoa học điên", "Nữ tu sĩ", "Hải tặc", 
    "Cung thủ thiện xạ", "Kẻ trộm bí ẩn", "Thợ săn tiền thưởng", "Tiều phu", "Đầu bếp", "Võ sư",
    "Chó Corgi", "Chó Husky", "Mèo Anh lông ngắn", "Mèo mun", "Sư tử đực", "Hổ trắng", "Báo gấm", 
    "Sói tuyết", "Gấu trúc", "Rồng lửa", "Phượng hoàng", "Kỳ lân (Unicorn)", "Đại bàng", "Cá mập trắng", 
    "Cáo chín đuôi", "Khủng long T-Rex", "Bướm khổng lồ", "Voi ma mút", "Chim ưng", "Rùa biển khổng lồ", 
    "Rắn hổ mang", "Ngựa hoang", "Cá voi xanh", "Hươu cao cổ", "Quạ đen", "Sứa phát sáng", "Nhện khổng lồ",
    "Siêu xe thể thao", "Xe máy cổ điển (Vespa)", "Xe mô tô phân khối lớn", "Tàu vũ trụ", "Tàu cướp biển", 
    "Trực thăng", "Robot Mecha khổng lồ", "Tàu ngầm", "Tàu hỏa hơi nước", "Khinh khí cầu", "Đĩa bay UFO", 
    "Xe tăng", "Tàu đệm từ", "Tàu lượn siêu tốc", "Ván trượt lơ lửng", "Thuyền thúng", "Xe ngựa kéo", "Phản lực cơ",
    "Thanh kiếm phát sáng", "Quyển sách ma thuật", "Tách cà phê bốc khói", "Đồng hồ quả quýt", "Vương miện đính đá", 
    "Lọ thuốc ma thuật", "Hộp nhạc", "Lâu đài Gothic", "Ngôi nhà gỗ trên cây", "Thành phố Cyberpunk", 
    "Trạm vũ trụ", "Đền thờ cổ đại", "Kim tự tháp", "Quán rượu thời trung cổ", "Trượng phép thuật", 
    "Gương thần", "Đèn cầy leo lét", "Ngọn hải đăng", "Cối xay gió", "Khách sạn ma ám", "Cầu treo", "Ngai vàng bằng sắt",
    "Ngọn núi lửa đang phun", "Cây thần thụ khổng lồ", "Thác nước phát sáng", "Cánh đồng hoa hướng dương", 
    "Bánh burger khổng lồ", "Ly cocktail nhiệt đới", "Vòi rồng", "Cực quang", "Bánh kem nhiều tầng", 
    "Tô mì ramen bốc khói", "Cây nấm độc sặc sỡ", "Tinh thể thạch anh khổng lồ"
]

dac_diem_opts = [
    "Mặc áo giáp kim loại", "Mặc vest sang trọng", "Mặc váy dạ hội lộng lẫy", "Mặc đồ phong cách Cyberpunk", "Mặc đồ truyền thống", "Đội nón lá", "Đội vương miện", "Đeo kính râm", "Đeo mặt nạ phòng độc", "Tóc dài tung bay", "Tóc ngắn cá tính", "Tóc màu bạch kim", "Tóc màu đỏ lửa", "Tóc màu neon", "Có sừng quỷ", "Có cánh thiên thần", "Có cánh ác quỷ/dơi", "Có đuôi", "Cơ bắp cuồn cuộn", "Mảnh khảnh", "Cơ thể khổng lồ", "Kích thước tí hon", "Làm bằng vàng nguyên khối", "Làm bằng pha lê/thủy tinh", "Làm bằng gỗ", "Làm bằng nước", "Làm bằng ngọn lửa", "Làm bằng băng tuyết", "Làm bằng máy móc/bánh răng", "Bị hỏng hóc/rách rưới", "Rỉ sét cổ kính", "Mới tinh bóng bẩy", "Tự phát sáng", "Cơ thể trong suốt", "Nhiều màu sắc sặc sỡ", "Chỉ có hai màu trắng đen", "Mắt đỏ ngầu", "Mắt xanh phát sáng", "Đang khóc nức nở", "Đang cười rạng rỡ", "Vẻ mặt tức giận", "Vẻ mặt buồn bã", "Vẻ mặt lạnh lùng/ngầu", "Cơ thể đầy máu/vết thương", "Dính bùn đất", "Ướt sũng nước", "Bao bọc bởi sấm sét", "Bao bọc bởi sương mù", "Bao bọc bởi hào quang", "Đeo trang sức lấp lánh", "Cầm vũ khí",
    "Tóc thắt bím", "Tóc tết dreadlock", "Mắt hai màu (Heterochromia)", "Có hình xăm phát sáng", "Mặc giáp vảy rồng", 
    "Mặc áo khoác trench coat", "Mặc sườn xám", "Đeo khuyên tai to bản", "Mặt đầy tàn nhang", "Da ngăm đen", 
    "Da trắng nhợt nhạt", "Có vết sẹo dài trên mặt", "Mọc sừng nai", "Có vầng hào quang sau đầu", "Bay lơ lửng nhờ từ trường", 
    "Đang tan chảy", "Làm bằng khói trắng", "Bọc trong kén pha lê", "Đeo bùa hộ mệnh", "Cầm gậy ma thuật", 
    "Cầm khiên năng lượng", "Đi chân trần", "Đi giày cao gót pha lê", "Đeo túi chéo techwear", "Mặc áo choàng tàng hình", 
    "Có đuôi cáo", "Có vảy cá lấp lánh", "Móng vuốt sắc nhọn", "Đeo mặt nạ hề", "Có răng nanh", 
    "Mắt máy móc", "Tay máy móc cyborg", "Đeo ba lô phản lực", "Có râu quai nón", "Mặc đồ phi hành gia", 
    "Mặc đồ lặn biển", "Mặc giáp hiệp sĩ Trung Cổ", "Đội mũ phớt", "Đội vương miện gai", "Có đôi tai yêu tinh (Elf)", 
    "Làm bằng kẹo bông gòn", "Làm bằng bánh quy", "Đính đầy hoa tươi", "Quấn đầy ruy băng", "Bị xích bằng dây xích sắt", 
    "Đeo nhẫn kim cương khổng lồ", "Mặc áo len oversize", "Cầm cuốn sổ tay cũ kỹ", "Đeo tai nghe chụp tai", "Cầm cọ vẽ", 
    "Mặc tạp dề lấm lem", "Mặc quân phục", "Cầm hoa hồng đen", "Thở ra sương giá"
]

hanh_dong_opts = [
    "Không chọn", "Đứng yên tĩnh lặng", "Ngồi thảnh thơi", "Nằm ườn ra", "Chạy nước rút", "Nhảy vọt lên cao", "Bay lượn trên không", "Bơi lặn dưới nước", "Đang chiến đấu ác liệt", "Vung kiếm chém", "Bắn súng", "Niệm thần chú ma thuật", "Đang ăn uống ngon miệng", "Đang đọc sách chăm chú", "Đang ngủ say", "Nhìn thẳng chằm chằm vào ống kính", "Nhìn xa xăm", "Chỉ tay về phía trước", "Nhảy múa uyển chuyển", "Đang lái xe/điều khiển phương tiện", "Đang rơi tự do", "Đang trèo vách núi/tường", "Cười lớn khoái chí", "La hét giận dữ", "Đang tan biến thành cát/bụi", "Đang dần bị đóng băng", "Đang bốc cháy ngùn ngụt", "Đang tạo dáng thời trang", "Đang gõ bàn phím/làm việc", "Bay xuyên qua tấm kính vỡ", "Lướt sóng trên dòng dung nham", "Hút linh hồn kẻ thù", "Đang lắp ráp vũ khí hạng nặng", "Nhảy breakdance cực sung", "Ngồi thiền lơ lửng giữa không trung", "Thưởng thức trà chiều sang chảnh", "Cưỡi chổi ma thuật vút đi", "Đang biến hình thành quái thú", "Phát nổ thành hàng triệu mảnh vụn ánh sáng", "Đang khóc ra những viên trân châu", "Cầm ô che cơn mưa sao băng", "Trượt tuyết với tốc độ xé gió", "Tung hứng những quả cầu lửa", "Thổi sáo gọi bầy chim chóc", "Đang pha chế độc dược sủi bọt", "Bị trói buộc bởi những dây leo ma thuật", "Phóng tia laser hủy diệt từ mắt", "Khám phá rương kho báu phát sáng", "Hấp thụ năng lượng từ mặt trời", "Bước qua cánh cổng không gian đa chiều", "Sửa chữa máy móc rỉ sét",
    "Đang tung cú đá xoay", "Đang né viên đạn (bullet time)", "Đang ôm mặt khóc", "Đang ngáp ngủ", "Đang vươn vai", 
    "Đang thì thầm vào tai", "Đang thổi nến sinh nhật", "Đang vuốt ve một con thú cưng", "Đang ném một quả bóng", "Đang bắt tay", 
    "Đang nháy mắt tinh nghịch", "Đang cắn môi", "Đang hôn gió", "Đang tung đồng xu", "Đang pha cà phê", 
    "Đang nướng thịt", "Đang tưới cây", "Đang đánh đàn guitar", "Đang kéo đàn violin", "Đang gõ trống", 
    "Đang vẽ tranh trên tường (graffiti)", "Đang lướt ván tuyết", "Đang nhảy dù", "Đang lặn ngắm san hô", "Đang cưỡi ngựa", 
    "Đang vung roi da", "Đang bắn cung", "Đang ném phi tiêu", "Đang thiền định dưới thác nước", "Đang đập vỡ một bức tường", 
    "Đang sửa chữa ô tô", "Đang bế một đứa trẻ", "Đang chỉ tay lên trời", "Đang đội mưa", "Đang che ô che nắng", 
    "Đang ngắm sao bằng kính viễn vọng", "Đang soi gương", "Đang xé một tờ giấy", "Đang đếm tiền", "Đang chơi cờ vua", 
    "Đang lắc vòng", "Đang tung hứng những chiếc nón", "Đang bị thổi bay bởi cuồng phong", "Đang trượt patin", "Đang đu dây thừng", 
    "Đang trốn trong bụi rậm", "Đang bò trên mặt đất", "Đang quỳ gối cầu nguyện", "Đang vấp ngã", "Đang bay vút lên bầu trời", 
    "Đang hạ cánh siêu anh hùng (superhero landing)", "Đang triệu hồi vòng tròn ma thuật", "Đang gầm rú thị uy"
]

boi_canh_opts = [
    "Không chọn", "Rừng nguyên sinh rậm rạp", "Khu rừng toàn nấm khổng lồ", "Sa mạc khô cằn nắng gắt", "Ốc đảo giữa sa mạc", "Hòn đảo hoang nhiệt đới", "Thành phố Cyberpunk tương lai ngập neon", "Thành phố đổ nát hậu tận thế", "Căn cứ trên Sao Hỏa", "Dưới đáy đại dương sâu thẳm", "Rạn san hô rực rỡ", "Lâu đài cổ kính rùng rợn", "Quán cà phê cổ điển ấm cúng", "Thư viện khổng lồ với vô số sách", "Phòng thí nghiệm khoa học hiện đại", "Đỉnh núi tuyết trắng xóa", "Trạm vũ trụ ngoài không gian", "Cánh đồng cỏ xanh mướt dưới bầu trời sao", "Khu chợ đêm sầm uất", "Phố lồng đèn châu Á", "Chiến trường rực lửa", "Trong một hang động pha lê", "Trên mặt trăng", "Phòng Studio phông nền trơn",
    "Bên trong một lỗ đen vũ trụ", "Thành phố lơ lửng trên chín tầng mây", "Ruộng bậc thang phát sáng trong đêm", "Sân ga tàu hỏa kéo dài vô tận", "Vương quốc làm hoàn toàn từ kẹo ngọt", "Nghĩa địa tàu vũ trụ khổng lồ", "Bên trong dạ dày của một con quái thú", "Trạm xăng bỏ hoang giữa sa mạc cát đỏ", "Thư viện ma thuật với những quyển sách trôi nổi", "Mê cung gương phản chiếu vô tận", "Đỉnh tháp đồng hồ Big Ben chìm trong sương mù", "Dòng sông dung nham cuồn cuộn chảy", "Bên trong một chiếc đồng hồ cơ học cổ đại", "Hành tinh toàn những khối pha lê tím", "Thành phố bong bóng dưới đáy biển", "Khu ổ chuột phong cách Steampunk đầy khói bụi", "Cánh đồng hoa bỉ ngạn đỏ rực rỡ", "Cung điện mùa đông làm từ băng tuyết nguyên khối", "Đấu trường La Mã rực lửa", "Bên trong một giọt nước khổng lồ", "Tàn tích của nền văn minh Atlantis"
]

phong_cach_opts = [
    "Không chọn", "Nhiếp ảnh tả thực (Photorealistic) - như ảnh chụp thật 8K", "Hoạt hình 3D (3D Render) - kiểu Pixar/Disney", "Anime/Manga - phong cách Nhật Bản 2D", "Ghibli Studio - phong cách anime thơ mộng", "Vẽ màu nước (Watercolor) - loang màu mềm mại", "Tranh sơn dầu (Oil Painting) - cổ điển, nét cọ dày", "Nghệ thuật Pixel (Pixel Art) - đồ họa game 8-bit", "Tối giản (Minimalism) - ít chi tiết, mảng màu lớn", "Cyberpunk - khoa học viễn tưởng ngầm", "Steampunk - viễn tưởng máy móc hơi nước thế kỷ 19", "Phác thảo bằng chì (Pencil Sketch) - đen trắng", "Pop Art - rực rỡ, tương phản cao kiểu truyện tranh Mỹ", "Đất sét (Claymation) - bóng bẩy, hình nặn thủ công", "Low Poly - tạo hình từ các khối đa giác", "Tranh khắc gỗ (Woodcut)", "Vẽ bằng mực nho (Sumi-e)",
    "Siêu thực (Surrealism) - ảo ảnh mộng mị như tranh Dali", "Vaporwave - tông màu hồng/tím retro thập niên 80", "Synthwave - viễn tưởng thập niên 80 với lưới neon", "Double Exposure - phơi sáng kép lồng 2 ảnh vào nhau", "Glitch Art - nghệ thuật nhiễu sóng kỹ thuật số", "Origami - vạn vật làm bằng giấy gấp nghệ thuật", "Gothic - kiến trúc đen tối, ma mị, hoa văn sắc sảo", "Art Deco - hình học đối xứng sang trọng thập niên 20"
]

anh_sang_opts = [
    "Không chọn", "Giờ vàng (Golden Hour) - ánh sáng vàng cam hoàng hôn/bình minh", "Giờ xanh (Blue Hour) - ánh sáng xanh dịu mát chập choạng tối", "Ánh sáng Studio (Studio Lighting) - đánh đèn chuyên nghiệp, mịn màng", "Ánh sáng điện ảnh (Cinematic Lighting) - tương phản sáng tối cao, nghệ thuật", "Ngược sáng (Backlighting) - nguồn sáng từ phía sau tạo viền", "Ánh sáng Neon (Neon Lighting) - xanh lá, đỏ, tím rực rỡ", "Ánh sáng tự nhiên (Natural Light) - trong trẻo, chân thực", "Ánh sáng âm u (Overcast/Gloomy) - nhiều mây, sáng đều, không bóng râm", "Ánh nến/Lửa (Candlelight/Firelight) - leo lét, ấm áp hắt từ dưới lên", "Tia sáng xuyên không (Volumetric Lighting / God Rays) - tia sáng xuyên qua sương/khe lá", "Ánh sáng gắt (Harsh Lighting) - nắng chói giữa trưa, bóng đổ đậm", "Phân cực (Bioluminescence) - ánh sáng sinh học phát sáng trong đêm", "Ánh trăng (Moonlight) - xanh ngắt, mờ ảo",
    "Ánh sáng lăng kính (Prism Lighting) - vệt sáng cầu vồng mộng mơ", "Ánh sáng tia chớp (Lightning Strike) - chớp nhoáng, tương phản cực gắt", "Ánh sáng tia laser (Laser Beams) - các luồng sáng cắt ngang không gian", "Bóng đổ hình học (Geometric Shadows) - bóng râm tạo thành hoa văn kỳ lạ", "Hào quang thần thánh (Ethereal Glow) - tỏa sáng rực rỡ từ bên trong"
]

goc_may_opts = [
    "Không chọn", "Cận cảnh (Close-up) - đặc tả khuôn mặt/chi tiết", "Chụp cực cận (Extreme Close-up) - dí sát vào một bộ phận rất nhỏ", "Bán thân (Medium Shot) - lấy từ thắt lưng trở lên", "Toàn cảnh (Wide Shot / Long Shot) - lấy toàn bộ chủ thể và bối cảnh rộng", "Từ trên xuống (Bird's-eye view) - nhìn thẳng từ trên trời xuống", "Từ dưới lên (Worm's-eye view) - hất từ mặt đất lên tạo sự vĩ đại", "Góc nhìn thứ nhất (POV) - nhìn qua đôi mắt của chính người xem", "Ngang tầm mắt (Eye-level shot) - góc nhìn thân thiện, trực diện", "Ống kính góc rộng (Wide-angle lens / Fisheye) - cong rìa ảnh, thu nhiều cảnh", "Chụp Macro (Macro photography) - phóng to vật siêu nhỏ", "Xóa phông mờ mịt (Depth of Field / Bokeh) - chỉ nét chủ thể", "Góc nghiêng (Dutch angle) - nghiêng máy ảnh tạo cảm giác chông chênh",
    "Nhìn qua vai (Over-the-shoulder) - đứng từ sau lưng nhìn tới", "Nhìn qua lỗ khóa (Keyhole view) - tò mò, bí ẩn", "Góc nhìn siêu vi (Microscopic view) - nhỏ bằng vi khuẩn", "Toàn cảnh 360 độ (Panoramic 360) - uốn cong không gian", "Đối xứng hoàn hảo (Perfect Symmetrical) - phong cách phim Wes Anderson", "Nhìn qua hình ảnh phản chiếu (Reflection) - qua mặt nước/gương"
]

khong_khi_opts = [
    "Bình yên, tĩnh lặng, thư thái", "Vui nhộn, tươi sáng, rộn ràng", "Bí ẩn, gây tò mò, mờ ảo", "Lãng mạn, ngọt ngào, ấm áp", "U ám, rùng rợn, giật gân, đáng sợ", "Mộng mơ, huyền ảo như cổ tích", "Hoài cổ (Nostalgic/Retro), màu úa vàng", "Hào hùng, sử thi, choángợp", "Sôi động, tốc độ, tràn đầy năng lượng", "Cô đơn, trống trải, tĩnh mịch", "Kịch tính, căng thẳng", "Thần tiên, ma thuật", "Sang trọng, quyền quý", "Cybernetic, máy móc lạnh lẽo",
    "Kỳ dị và điên rồ (Whimsical/Bizarre)", "Ngột ngạt và khép kín (Claustrophobic)", "Thiêng liêng và thanh tẩy (Divine/Holy)", "Hoang tàn hậu tận thế (Apocalyptic)", "Choáng ngợp tâm lý (Psychedelic)", "U sầu và tiếc nuối (Melancholic)"
]

mau_sac_opts = [
    "Không chọn",
    "Trắng đen (Black & White) - Cổ điển, tương phản",
    "Đơn sắc (Monochrome) - Chỉ dùng các sắc độ của một màu",
    "Màu Pastel nhẹ nhàng - Ngọt ngào, dịu mắt",
    "Sặc sỡ, rực rỡ (Vibrant/Colorful) - Năng động, bắt mắt",
    "Tông màu lạnh (Cool tones) - Xanh dương, lục, tím ngắt",
    "Tông màu ấm (Warm tones) - Đỏ, cam, vàng rực",
    "Màu Sepia hoài cổ - Sắc nâu vàng của ảnh cũ",
    "Màu Neon phát sáng - Rực rỡ trong đêm",
    "Màu Cyberpunk - Xanh ngọc và hồng/tím chói lóa",
    "Màu Retro thập niên 80 - Phai màu, nhiễu hạt",
    "Màu tương phản cao (High Contrast) - Đậm đà, sắc nét",
    "Tông màu trầm/phai (Muted/Desaturated) - U buồn, điện ảnh",
    "Màu hoàng kim (Golden/Champagne) - Sang trọng, lấp lánh"
]

# Câu lệnh yêu cầu AI đã được cập nhật, bỏ ghi chú dư thừa ra khỏi luồng prompt
bat_buoc_opts = [
    "NGHIÊM CẤM THAY ĐỔI KHUÔN MẶT: Giữ nguyên 100% hình dáng, đường nét, biểu cảm nét mặt và góc độ khuôn mặt của chủ thể trong ảnh gốc. Không được tự ý làm đẹp, bóp méo hay biến dạng.",
    "Tuyệt đối không có chữ viết, văn bản hay watermark trong ảnh",
    "Giữ đúng màu sắc và kết cấu trang phục của ảnh gốc",
    "Không làm biến dạng tay, chân, ngón tay của chủ thể",
    "Hình ảnh phải sắc nét ở độ phân giải cao nhất (8K, cực kỳ chi tiết)",
    "Chỉ xuất hiện duy nhất 1 chủ thể, không có nhân vật phụ",
    "Giữ nguyên bối cảnh nền của ảnh gốc, chỉ thay đổi chủ thể"
]

ty_le_opts = [
    "Không chọn",
    "1:1 (Ảnh Vuông - Mặc định)",
    "16:9 (Ảnh Ngang - Widescreen/Youtube)",
    "9:16 (Ảnh Dọc - Story/Reels/Tiktok)",
    "4:3 (Ngang tiêu chuẩn)",
    "3:4 (Dọc tiêu chuẩn)",
    "21:9 (Ngang siêu rộng - Cinematic)"
]

def add_edit_item():
    st.session_state.edit_items.append({"element": "", "level": "Không thay đổi"})

def add_merge_image():
    st.session_state.merge_images.append(f"Ảnh {len(st.session_state.merge_images) + 1}")

def xu_ly_chuoi(chuoi):
    try:
        if " - " in chuoi: return chuoi.split(" - ")[0]
        if ": " in chuoi: return chuoi.split(": ")[0]
        return chuoi
    except Exception:
        return chuoi

# --- GIAO DIỆN CHUNG ---
def ui_chung():
    st.subheader("⚙️ Cài đặt cơ bản cho Prompt")
    
    r_key = st.session_state.reset_key

    st.markdown("**📏 Thiết lập Khung hình & Chủ thể**")
    col_sub0, col_sub1, col_sub2 = st.columns([1, 1.5, 1.5])
    with col_sub0:
        ty_le_anh = st.selectbox("🖼️ Tỷ lệ ảnh:", ty_le_opts, key=f"ty_le_{r_key}")
    with col_sub1:
        chu_the = st.selectbox("1. 👤 Chủ thể chính:", chu_the_opts, key=f"chu_the_{r_key}")
        chu_the_tu_nhap = st.text_input("✍️ Tự nhập chủ thể:", placeholder="VD: Một chú chim cánh cụt...", key=f"chu_the_nhap_{r_key}")
    with col_sub2:
        dac_diem = st.multiselect("✨ Đặc điểm của chủ thể:", dac_diem_opts, placeholder="Chọn một hoặc nhiều đặc điểm...", key=f"dac_diem_{r_key}")
        dac_diem_khac = st.text_input("✍️ Tự nhập đặc điểm khác:", key=f"dac_diem_khac_{r_key}")

    st.markdown("**✨ Thiết lập Chi tiết**")
    col1, col2 = st.columns(2)
    with col1:
        hanh_dong = st.selectbox("2. 🏃 Hành động/Trạng thái:", hanh_dong_opts, key=f"hanh_dong_{r_key}")
        hanh_dong_tu_nhap = st.text_input("✍️ Tự nhập hành động:", key=f"hanh_dong_nhap_{r_key}")
        
        phong_cach = st.selectbox("4. 🎭 Phong cách nghệ thuật:", phong_cach_opts, key=f"phong_cach_{r_key}")
        phong_cach_tu_nhap = st.text_input("✍️ Tự nhập phong cách:", key=f"phong_cach_nhap_{r_key}")
        
        goc_may = st.selectbox("6. 📐 Góc máy & Bố cục:", goc_may_opts, key=f"goc_may_{r_key}")
        goc_may_tu_nhap = st.text_input("✍️ Tự nhập góc máy:", key=f"goc_may_nhap_{r_key}")
        
        mau_sac = st.selectbox("8. 🎨 Màu sắc chủ đạo:", mau_sac_opts, key=f"mau_sac_{r_key}")
        mau_sac_tu_nhap = st.text_input("✍️ Tự nhập màu sắc:", key=f"mau_sac_nhap_{r_key}")
        
    with col2:
        boi_canh = st.selectbox("3. 🏞️ Bối cảnh (Setting):", boi_canh_opts, key=f"boi_canh_{r_key}")
        boi_canh_tu_nhap = st.text_input("✍️ Tự nhập bối cảnh:", key=f"boi_canh_nhap_{r_key}")
        
        anh_sang = st.selectbox("5. 💡 Ánh sáng (Lighting):", anh_sang_opts, key=f"anh_sang_{r_key}")
        anh_sang_tu_nhap = st.text_input("✍️ Tự nhập ánh sáng:", key=f"anh_sang_nhap_{r_key}")
        
        khong_khi = st.multiselect("7. 🌤️ Bầu không khí (Mood/Vibe):", khong_khi_opts, placeholder="Chọn các bầu không khí kết hợp...", key=f"khong_khi_{r_key}")
        khong_khi_tu_nhap = st.text_input("✍️ Tự nhập không khí (nếu có):", key=f"khong_khi_nhap_{r_key}")

    st.markdown("---")
    du_lieu_phan_tich = st.text_area("🔮 **Kế thừa Thông Số Ảnh Cũ:** Nếu bạn đã dùng chức năng 'Phân tích ảnh', hãy dán kết quả AI trả về vào đây. AI sẽ tự động đắp các thông số đó vào ảnh mới, bạn không cần phải chọn thêm thông số nào.", height=100, key=f"du_lieu_phan_tich_{r_key}")

    st.markdown("---")
    st.subheader("📌 Yêu cầu bổ sung")
    bat_buoc = st.multiselect("🛑 Các yêu cầu AI TUYỆT ĐỐI BẮT BUỘC tuân thủ:", bat_buoc_opts, placeholder="Chọn các yêu cầu bắt buộc...", key=f"bat_buoc_{r_key}")
    
    # Hiển thị ghi chú cho người dùng thấy nhưng không đưa vào Prompt của AI
    st.info("💡 Lưu ý nhỏ cho bạn: Nếu bạn chọn yêu cầu 'Giữ nguyên khuôn mặt' nhưng lại muốn AI đổi góc nhìn của chủ thể (ví dụ từ nhìn thẳng sang nhìn nghiêng), bạn phải tải kèm thêm bức ảnh mẫu cung cấp góc mặt nghiêng đó lên nhé!")
    
    bat_buoc_khac = st.text_area("✍️ Tự nhập thêm yêu cầu bắt buộc / tuyệt đối tránh:", key=f"bat_buoc_khac_{r_key}")
    
    so_luong = st.number_input("🔢 Số lượng ảnh cần tạo:", min_value=1, value=1, key=f"so_luong_{r_key}")
    
    return {
        "ty_le_anh": ty_le_anh,
        "chu_the": chu_the, "chu_the_tu_nhap": chu_the_tu_nhap, "dac_diem": dac_diem, "dac_diem_khac": dac_diem_khac,
        "hanh_dong": hanh_dong, "hanh_dong_tu_nhap": hanh_dong_tu_nhap, "boi_canh": boi_canh, "boi_canh_tu_nhap": boi_canh_tu_nhap, 
        "phong_cach": phong_cach, "phong_cach_tu_nhap": phong_cach_tu_nhap, "anh_sang": anh_sang, "anh_sang_tu_nhap": anh_sang_tu_nhap, 
        "goc_may": goc_may, "goc_may_tu_nhap": goc_may_tu_nhap, "khong_khi": khong_khi, 
        "khong_khi_tu_nhap": khong_khi_tu_nhap, "mau_sac": mau_sac, "mau_sac_tu_nhap": mau_sac_tu_nhap, 
        "du_lieu_phan_tich": du_lieu_phan_tich, "bat_buoc": bat_buoc, 
        "bat_buoc_khac": bat_buoc_khac, "so_luong": so_luong
    }

# Hàm lắp ráp dữ liệu thành câu lệnh mượt mà
def tao_prompt(data, context="tao_moi", thong_tin_sua=""):
    try:
        prompt = ""
        if context == "tao_moi":
            prompt += f"Hãy tạo {data['so_luong']} bức ảnh với các yêu cầu chi tiết sau:\n\n"
        elif context == "sua_anh":
            prompt += f"Sử dụng bức ảnh tôi vừa đính kèm làm tài liệu tham khảo chính. Hãy tạo ra {data['so_luong']} bức ảnh mới dựa trên ảnh gốc với các yêu cầu chỉnh sửa sau:\n\n"
            prompt += thong_tin_sua + "\n\n"
            prompt += "Các thông số thiết lập cho bức ảnh mới:\n"
        elif context == "ghep_anh":
            prompt += f"Sử dụng các bức ảnh tôi vừa đính kèm làm tài liệu tham khảo chính. Hãy ghép chúng lại và tạo ra {data['so_luong']} bức ảnh mới với các chỉ thị sau:\n\n"
            prompt += thong_tin_sua + "\n\n"
            prompt += "Các thông số thiết lập cho bức ảnh mới:\n"
            
        if data.get('ty_le_anh') and data['ty_le_anh'] != "Không chọn":
            prompt += f"Tỷ lệ khung hình: {xu_ly_chuoi(data['ty_le_anh'])}\n"
            
        c_chu_the = data['chu_the_tu_nhap'] if data['chu_the_tu_nhap'] else data['chu_the']
        c_hanh_dong = data['hanh_dong_tu_nhap'] if data['hanh_dong_tu_nhap'] else data['hanh_dong']
        c_boi_canh = data['boi_canh_tu_nhap'] if data['boi_canh_tu_nhap'] else data['boi_canh']
        c_phong_cach = data['phong_cach_tu_nhap'] if data['phong_cach_tu_nhap'] else data['phong_cach']
        c_anh_sang = data['anh_sang_tu_nhap'] if data['anh_sang_tu_nhap'] else data['anh_sang']
        c_goc_may = data['goc_may_tu_nhap'] if data['goc_may_tu_nhap'] else data['goc_may']
        c_mau_sac = data['mau_sac_tu_nhap'] if data['mau_sac_tu_nhap'] else data['mau_sac']

        if c_chu_the and c_chu_the != "Không chọn": 
            prompt += f"Chủ thể chính: {xu_ly_chuoi(c_chu_the)}\n"
        
        list_dd = data['dac_diem'].copy()
        if data['dac_diem_khac']: list_dd.append(data['dac_diem_khac'])
        if list_dd: prompt += f"Đặc điểm chủ thể: {', '.join(list_dd)}\n"

        if c_hanh_dong and c_hanh_dong != "Không chọn": 
            prompt += f"Hành động: {xu_ly_chuoi(c_hanh_dong)}\n"
        if c_boi_canh and c_boi_canh != "Không chọn": 
            prompt += f"Bối cảnh: {xu_ly_chuoi(c_boi_canh)}\n"
        if c_phong_cach and c_phong_cach != "Không chọn": 
            prompt += f"Phong cách nghệ thuật: {xu_ly_chuoi(c_phong_cach)}\n"
        if c_anh_sang and c_anh_sang != "Không chọn": 
            prompt += f"Ánh sáng: {xu_ly_chuoi(c_anh_sang)}\n"
        if c_goc_may and c_goc_may != "Không chọn": 
            prompt += f"Góc máy và bố cục: {xu_ly_chuoi(c_goc_may)}\n"
        if c_mau_sac and c_mau_sac != "Không chọn": 
            prompt += f"Màu sắc chủ đạo: {xu_ly_chuoi(c_mau_sac)}\n"
        
        list_kk = data['khong_khi'].copy()
        if data['khong_khi_tu_nhap']: list_kk.append(data['khong_khi_tu_nhap'])
        if list_kk: prompt += f"Bầu không khí: {', '.join(list_kk)}\n"
        
        # Chỉ dán trực tiếp dữ liệu phân tích cũ vào, bỏ các câu tiêu đề thừa thãi
        if data.get('du_lieu_phan_tich') and data['du_lieu_phan_tich'].strip() != "":
            prompt += f"\n{data['du_lieu_phan_tich'].strip()}\n"
        
        list_bb = data['bat_buoc'].copy()
        if data['bat_buoc_khac']: list_bb.append(data['bat_buoc_khac'])
        if list_bb: 
            prompt += f"\nYêu cầu RÀNG BUỘC TUYỆT ĐỐI (Bắt buộc phải tuân theo 100%):\n"
            for idx, req in enumerate(list_bb, 1):
                prompt += f"{idx}. {req}\n"
                
        return prompt
    except Exception as e:
        return f"Ui cha, có lỗi lúc tạo prompt rồi: {e}"

# --- MAIN APP ---
st.title("🌟 Ứng dụng Tạo Prompt Ảnh Tự Động")

col_header1, col_header2 = st.columns([4, 1])
with col_header2:
    st.button("🗑️ Xóa thông tin (Clear All)", on_click=xoa_toan_bo, use_container_width=True)

task = st.radio("🛠️ Chọn thao tác bạn muốn thực hiện:", [
    "🎨 Tạo ảnh mới hoàn toàn", 
    "✏️ Chỉnh sửa ảnh có sẵn", 
    "🧩 Ghép các ảnh có sẵn", 
    "🔍 Phân tích ảnh"
], horizontal=True)
st.divider()

r_key = st.session_state.reset_key

try:
    if task == "🎨 Tạo ảnh mới hoàn toàn":
        data = ui_chung()
        if st.button("🚀 Tạo Prompt", type="primary"):
            ket_qua = tao_prompt(data, context="tao_moi")
            st.success("🎉 Tạo prompt thành công! Bấm vào nút Copy (biểu tượng hai tờ giấy) ở góc trên bên phải khung xám để chép nhé.")
            st.code(ket_qua, language="text")

    elif task == "✏️ Chỉnh sửa ảnh có sẵn":
        st.info("💡 Hệ thống sẽ tự động yêu cầu AI phân tích và sử dụng ảnh đính kèm của bạn.")
        
        st.write("**🔧 Tùy chỉnh yếu tố trong ảnh:**")
        for i, item in enumerate(st.session_state.edit_items):
            c1, c2 = st.columns([2, 1])
            with c1: st.session_state.edit_items[i]["element"] = st.text_input(f"🎯 Yếu tố cần sửa {i+1}", value=item["element"], key=f"el_{i}_{r_key}", placeholder="VD: Gương mặt, chiếc áo, phông nền...")
            with c2: st.session_state.edit_items[i]["level"] = st.selectbox(f"🎚️ Mức độ", ["Không thay đổi", "Thay đổi ít", "Thay đổi nhiều", "Thay đổi hoàn toàn"], index=["Không thay đổi", "Thay đổi ít", "Thay đổi nhiều", "Thay đổi hoàn toàn"].index(item["level"] if item["level"] in ["Không thay đổi", "Thay đổi ít", "Thay đổi nhiều", "Thay đổi hoàn toàn"] else "Không thay đổi"), key=f"lv_{i}_{r_key}")
        st.button("➕ Thêm yếu tố cần chỉnh sửa", on_click=add_edit_item)
        
        col_x, col_t = st.columns(2)
        with col_x: xoa_dt = st.text_input("🗑️ Đối tượng muốn XÓA hoàn toàn khỏi ảnh gốc:", key=f"xoa_dt_{r_key}")
        with col_t: them_dt = st.text_input("🌟 Đối tượng muốn THÊM mới vào ảnh:", key=f"them_dt_{r_key}")
        
        st.divider()
        data = ui_chung()
        
        if st.button("🚀 Tạo Prompt", type="primary"):
            thong_tin_sua = ""
            for item in st.session_state.edit_items:
                if item["element"]: thong_tin_sua += f"Chỉnh sửa '{item['element']}' ở mức độ: {item['level']}\n"
            if xoa_dt: thong_tin_sua += f"Xóa hoàn toàn khỏi ảnh: {xoa_dt}\n"
            if them_dt: thong_tin_sua += f"Thêm đối tượng mới vào ảnh: {them_dt}\n"
            
            ket_qua = tao_prompt(data, context="sua_anh", thong_tin_sua=thong_tin_sua.strip())
            st.success("🎉 Nhớ đính kèm bức ảnh bạn cần sửa nhé! Bấm nút Copy góc phải khung dưới đây:")
            st.code(ket_qua, language="text")

    elif task == "🧩 Ghép các ảnh có sẵn":
        st.info("💡 Hệ thống sẽ tự động yêu cầu AI tham khảo các ảnh bạn đính kèm.")
        
        st.write("**🖼️ Mô tả các ảnh đính kèm:**")
        for i, img_name in enumerate(st.session_state.merge_images):
            st.text_input(f"📝 Mô tả tóm tắt {img_name}:", key=f"desc_{i}_{r_key}", placeholder=f"VD: Đây là ảnh phong cảnh / Đây là ảnh cô gái...")
        st.button("➕ Thêm Ảnh đính kèm (Ảnh 3, Ảnh 4...)", on_click=add_merge_image)
        
        st.write("**🛠️ Thiết lập cách ghép:**")
        giu_chi_tiet = st.text_input("✂️ Chi tiết cần GIỮ LẠI / BÓC TÁCH (VD: Cắt lấy người ở Ảnh 1 giữ nguyên mặt):", key=f"giu_chi_tiet_{r_key}")
        tuong_tac = st.text_area("🔄 Tương tác/Vị trí không gian (VD: Đặt người ở Ảnh 1 ngồi lên chiếc ghế trong Ảnh 2):", key=f"tuong_tac_{r_key}")
        
        st.divider()
        data = ui_chung()
        
        if st.button("🚀 Tạo Prompt", type="primary"):
            thong_tin_ghep = ""
            for i, img_name in enumerate(st.session_state.merge_images):
                desc = st.session_state.get(f"desc_{i}_{r_key}", "")
                if desc: thong_tin_ghep += f"{img_name}: {desc}\n"
                
            thong_tin_ghep += f"Yêu cầu bóc tách chi tiết: {giu_chi_tiet}\n"
            thong_tin_ghep += f"Vị trí và tương tác giữa các ảnh: {tuong_tac}\n"
                
            ket_qua = tao_prompt(data, context="ghep_anh", thong_tin_sua=thong_tin_ghep.strip())
            st.success("🎉 Nhớ tải tất cả các ảnh lên theo đúng thứ tự. Bấm nút Copy góc phải khung xám bên dưới:")
            st.code(ket_qua, language="text")

    elif task == "🔍 Phân tích ảnh":
        st.info("🔍 Hãy đưa ảnh cho AI soi thật kỹ xem bên trong có gì nhé!")
        if st.button("🚀 Tạo Prompt Phân Tích", type="primary"):
            # Yêu cầu AI chỉ trả về text thuần, không format rườm rà
            prompt_pt = "Hãy đóng vai là một chuyên gia phân tích hình ảnh. Hãy soi thật kỹ bức ảnh tôi vừa đính kèm và mô tả lại một cách cực kỳ chi tiết tất cả các yếu tố xuất hiện trong ảnh. Bắt buộc bao gồm các yếu tố sau: Chủ thể chính, Hành động, Đặc điểm nổi bật, Bối cảnh xung quanh, Phong cách nghệ thuật, Cách sắp đặt ánh sáng, Màu sắc chủ đạo, Góc máy ảnh/Bố cục, Bầu không khí chung và Tỷ lệ khung hình của bức ảnh.\n\nCHỈ THỊ NGHIÊM NGẶT: Bạn CHỈ ĐƯỢC trả về một đoạn văn bản thuần túy (plain text), các thông tin nối tiếp nhau hoặc cách nhau bởi dấu phẩy. TUYỆT ĐỐI KHÔNG sử dụng ký tự định dạng markdown như dấu sao (**) để in đậm, KHÔNG dùng gạch đầu dòng (- hay *), KHÔNG xuống dòng không cần thiết. KHÔNG mở bài chào hỏi, KHÔNG kết luận, KHÔNG khuyên bảo."
            st.success("🎉 Bạn rà chuột vào góc trên cùng bên phải của ô xám bên dưới, nhấn vào biểu tượng Copy là xong:")
            st.code(prompt_pt, language="text")

except Exception as e:
    st.error(f"Ối, ứng dụng đang bị vấp một chút: {e}")
