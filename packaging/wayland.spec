Name:		wayland
Version:	1.0.6
Release:	0
Summary:	Wayland Compositor Infrastructure
License:	MIT
Group:		Graphics/Wayland Window System
URL:		http://wayland.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/wayland/wayland
#Git-Web:	http://cgit.freedesktop.org/wayland/wayland/
Source:		%name-%version.tar.xz
BuildRequires:	autoconf >= 2.64, automake >= 1.11
BuildRequires:	libtool >= 2.2
BuildRequires:	pkgconfig
BuildRequires:  pkgconfig(libffi)
BuildRequires:  expat-devel
BuildRequires:  xz
BuildRequires:  doxygen

%description
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package -n libwayland-client
Group:		Graphics/Wayland Window System
Summary:	Wayland core client library

%description -n libwayland-client
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package -n libwayland-cursor
Group:		Graphics/Wayland Window System
Summary:	Wayland cursor library

%description -n libwayland-cursor
The purpose of this library is to be the equivalent of libXcursor in
the X world. This library is compatible with X cursor themes and
loads them directly into an shm pool making it easy for the clients
to get buffer for each cursor image.

%package -n libwayland-server
Group:		Graphics/Wayland Window System
Summary:	Wayland core server library

%description -n libwayland-server
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package devel
Summary:	Development files for the Wayland Compositor Infrastructure
Group:		Development/Libraries
Requires:	libwayland-client = %version
Requires:	libwayland-cursor = %version
Requires:	libwayland-server = %version

%description devel
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q

%build
%autogen
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%post -n libwayland-client -p /sbin/ldconfig
%postun -n libwayland-client -p /sbin/ldconfig
%post -n libwayland-cursor -p /sbin/ldconfig
%postun -n libwayland-cursor -p /sbin/ldconfig
%post -n libwayland-server -p /sbin/ldconfig
%postun -n libwayland-server -p /sbin/ldconfig

%files -n libwayland-client
%defattr(-,root,root)
%_libdir/libwayland-client.so.0*

%files -n libwayland-cursor
%defattr(-,root,root)
%_libdir/libwayland-cursor.so.0*

%files -n libwayland-server
%defattr(-,root,root)
%_libdir/libwayland-server.so.0*

%files devel
%defattr(-,root,root)
%_bindir/wayland-scanner
%_includedir/wayland-*.h
%_libdir/libwayland-*.so
%_libdir/pkgconfig/wayland-*.pc
%_datadir/aclocal

%changelog